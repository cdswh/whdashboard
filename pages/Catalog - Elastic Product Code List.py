import streamlit as st
import ssl
from PIL import Image
from urllib.request import urlopen
import pickle
import streamlit_authenticator as stauth
from pathlib import Path

ssl._create_default_https_context = ssl._create_unverified_context

st.set_page_config(layout="wide")

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
    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    imageLOGO = Image.open(urlopen("https://i.ibb.co/WGjVK32/logopng.png"))
    st.image(imageLOGO)

    st.sidebar.header(f"Welcome {name}")
    authenticator.logout("Signout", "sidebar")
    device_names = [
        "Arrow QG w/ CAN",
        "Arrow QG w/o CAN",
        "Arrow VI w/ CAN",
        "Arrow VI w/o CAN",
        "Dagger-LG",
        "Dagger-QG Large",
        "Arrow-L",
        "Arrow-LX",
        "Arrow-M (Cat-M)",
        "Arrow-67",
        "Arrow-C (CDMA)",
        "Arrow-G (2G)",
        "Arrow-H (3G)",
    ]
    selected_code = st.sidebar.selectbox("Select a device:", device_names)

    st.title("Catalog - Elastic Product Codes")
    st.markdown("")

    if selected_code == "Arrow QG w/ CAN":
        st.markdown("**Arrow QG w/ CAN T-Mobile**")
        st.code(
            """
        Product code: 4-6340-10
Type: NC-GVI-TM
    """
        )
        st.markdown("---")

        st.markdown("**Arrow QG w/ CAN Verizon**")
        st.code(
            """
        Product code: 4-6340-17
Type: NC-GVI-VZ
    """
        )
        st.markdown("---")

        st.markdown("**Arrow QG w/ CAN AerisPro**")
        st.code(
            """
        Product code: 4-6340-520
Type: NC-GVI-AP
    """
        )

    if selected_code == "Arrow QG w/o CAN":
        st.markdown("**Arrow QG w/o CAN - T-Mobile**")
        st.code(
            """
        Product code: 4-6341-10
Type: NC-GVIXV-TM
    """
        )
        st.markdown("---")

        st.markdown("**Arrow QG w/o CAN - Verizon**")
        st.code(
            """
        Product code: 4-6341-17
Type: NC-GVIXV-VZ
    """
        )
        st.markdown("---")

        st.markdown("**Arrow QG w/o CAN - AerisPro**")
        st.code(
            """
        Product code: 4-6341-520
Type: NC-GVIXV-AP
    """
        )

    if selected_code == "Arrow VI w/ CAN":
        st.markdown("**Arrow VI w/ CAN - T-Mobile**")
        st.code(
            """
        Product code: 4-6350-10
Type: NC-QHM-TM
    """
        )
        st.markdown("---")

        st.markdown("**Arrow VI w/ CAN - Verizon**")
        st.code(
            """
        Product code: 4-6350-17
Type: NC-QHM-VZ
    """
        )
        st.markdown("---")

        st.markdown("**Arrow VI w/ CAN - AerisPro**")
        st.code(
            """
        Product code: 4-6350-520
Type: NC-HQ-AP
    """
        )

    if selected_code == "Arrow VI w/o CAN":
        st.markdown("**Arrow VI w/o CAN - T-Mobile**")
        st.code(
            """
        Product code: 4-6351-10
Type: NC-HQXV-TM
    """
        )
        st.markdown("---")

        st.markdown("**Arrow VI w/o CAN - Verizon**")
        st.code(
            """
        Product code: 4-6351-17
Type: NC-HQXV-VZ
    """
        )
        st.markdown("---")

        st.markdown("**Arrow VI w/o CAN - AerisPro**")
        st.code(
            """
        Product code: 4-6351-520
Type: NC-HQXV-AP
    """
        )

    if selected_code == "Dagger-LG":
        st.markdown("**Dagger-LG - T-Mobile**")
        st.code(
            """
        Product code: 4-6412-10
Type: DG-SS4K-TM
    """
        )

    if selected_code == "Dagger-QG Large":
        st.markdown("**Dagger-QG Large - T-Mobile**")
        st.code(
            """
        Product code: 4-6415-510
Type: DG-QGL-TM
    """
        )
        st.markdown("---")

        st.markdown("**Dagger-QG Large - AerisPro**")
        st.code(
            """
        Product code: 4-6415-520
Type: DG-QGL-AP
    """
        )

    if selected_code == "Arrow-L":
        st.markdown("**Arrow-L - T-Mobile**")
        st.code(
            """
        Product code: 4-6510-10
Type: NC-ARL-TM
    """
        )
        st.markdown("---")

        st.markdown("**Arrow-L - AerisPro**")
        st.code(
            """
        Product code: 4-6510-520
Type: NC-ARL-AP
    """
        )

    if selected_code == "Arrow-LX":
        st.markdown("**Arrow-LX - T-Mobile**")
        st.code(
            """
        Product code: 4-6511-10
Type: NC-ARLX-TM
    """
        )
        st.markdown("---")

        st.markdown("**Arrow-LX - AerisPro**")
        st.code(
            """
        Product code: 4-6511-520
Type: NC-ARL-AP
    """
        )

    if selected_code == "Arrow-M (Cat-M)":
        st.markdown("**Arrow-M (Cat-M) - Verizon**")
        st.code(
            """
        Product code: 4-6520-17
Type: NC-ARM-VZ
    """
        )

    if selected_code == "Arrow-67":
        st.markdown("**Arrow-67 (PowerSports) - T-Mobile**")
        st.code(
            """
        Product code: 4-7320-10
Type: PS-ARL-TM
    """
        )

    if selected_code == "Arrow-C (CDMA)":
        st.markdown("**Arrow-C - Verizon**")
        st.code(
            """
        Product code: 4-7520-17
Type: ARROWC-V
    """
        )

    if selected_code == "Arrow-G (2G)":
        st.markdown("**Arrow-G - Aeris**")
        st.code(
            """
        Product code: 4-7521-04
Type: ARROWG-A
    """
        )
        st.markdown("---")

        st.markdown("**Arrow-G - Telefonica**")
        st.code(
            """
        Product code: 4-7521-05
Type: ARROWG-T
    """
        )

    if selected_code == "Arrow-H (3G)":
        st.markdown("**Arrow-H - Aeris**")
        st.code(
            """
        Product code: 4-7522-04
Type: ARROWH-A
    """
        )

        st.markdown("---")
        st.markdown("**Arrow-H - Telefonica**")
        st.code(
            """
        Product code: 4-7522-05
Type: ARROWH-T
    """
        )

    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    st.warning("Please enter your username and password")
