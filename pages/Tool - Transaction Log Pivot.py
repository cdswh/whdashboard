import pandas as pd
import streamlit as st
from PIL import Image
from urllib.request import urlopen
import pickle
import streamlit_authenticator as stauth
from pathlib import Path
from datetime import datetime
from datetime import timedelta
from datetime import date
import ssl
import pickle
from pathlib import Path

current_dateTime = datetime.now()
start_dateTime = date(2022, 12, 1)

st.set_page_config(layout="wide")
# Hide 'Made with Streamlit' & app menu
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# --- USER AUTHENTICATION ---
names = ["Paul Vergara", "Jesus Lopez", "Kristen Hale", "Josh Santana"]
usernames = ["pvergara", "jlopez", "khale", "jsantana"]

# load hashed passwords
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

credentials = {"usernames": {}}

for uname, name, pwd in zip(usernames, names, hashed_passwords):
    user_dict = {"name": name, "password": pwd}
    credentials["usernames"].update({uname: user_dict})

authenticator = stauth.Authenticate(
    credentials, "cds_pack", "guW70qH9RX", cookie_expiry_days=30
)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status:
    ssl._create_default_https_context = ssl._create_unverified_context

    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    st.markdown("---")
    uploaded_file = st.file_uploader(
        "Choose a file (Excel or CSV)", type=["xlsx", "csv"]
    )
    st.warning(
        """To get an accurate count of the number of devices shipped, 
           please edit your Excel or CSV file to include only the dates you want 
           to include in the count."""
    )

    if uploaded_file is not None:
        file_name = uploaded_file.name
        if file_name.endswith(".csv"):
            df = pd.read_csv(uploaded_file, engine="python")
        elif file_name.endswith(".xlsx"):
            df = pd.read_excel(uploaded_file)
        else:
            st.write("Error: Unsupported file type.")
        df = df.applymap(lambda x: x.replace('"', "") if isinstance(x, str) else x)
        df = df[~df["Code"].isin(["3-SHIP", "3-COD", "3-TAX", "9-2001"])]
        df["Code"] = df["Code"].apply(lambda x: x[:-5] if x.count("-") == 3 else x)
        pivot = df.pivot_table(index="Code", values="Qty", aggfunc="sum")
        st.dataframe(pivot)


if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    st.warning("Please enter your username and password")
