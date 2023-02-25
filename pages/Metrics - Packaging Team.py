import pandas as pd
import gspread
import streamlit as st
from PIL import Image
from urllib.request import urlopen
import pickle
import streamlit_authenticator as stauth
from pathlib import Path
from datetime import datetime
from datetime import date
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

    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive",
    ]

    client = gspread.service_account(filename="service_account.json")
    database = client.open("Database")

    # gspread.sheets
    pt_ind = database.worksheet("individual")
    pt_bulk = database.worksheet("bulk")
    pt_adv = database.worksheet("advantage")
    pt_mtd = database.worksheet("MTD")

    # gspread.getrocords
    advantage = pd.DataFrame(pt_adv.get_all_records())
    bulk = pd.DataFrame(pt_bulk.get_all_records())
    individual = pd.DataFrame(pt_ind.get_all_records())

    # individual packaging
    i_date = individual["Date"]
    i_tony = int(sum(individual["Tony"]))
    i_luis = int(sum(individual["Luis"]))
    i_alexsamm = int(sum(individual["Alex"]))
    i_andy = int(sum(individual["Andy"]))
    i_mario = int(sum(individual["Mario"]))
    i_anfernnie = int(sum(individual["Anfernnie"]))
    i_daejon = int(sum(individual["Daejon"]))
    i_jose = int(sum(individual["Jose"]))

    # bulk packaging
    b_tony = int(sum(bulk["Tony"]))
    b_luis = int(sum(bulk["Luis"]))
    b_alexsamm = int(sum(bulk["Alex"]))
    b_andy = int(sum(bulk["Andy"]))
    b_mario = int(sum(bulk["Mario"]))
    b_anfernnie = int(sum(bulk["Anfernnie"]))
    b_daejon = int(sum(bulk["Daejon"]))
    b_jose = int(sum(bulk["Jose"]))

    # advantage packaging
    david_evo = int(sum(advantage["David EVO"]))
    david_revo = int(sum(advantage["David REVO"]))
    marco_evo = int(sum(advantage["Marco EVO"]))
    marco_revo = int(sum(advantage["Marco REVO"]))

    # mtd total
    mtd_tony = int(pt_mtd.cell(2, 1).value)
    mtd_luis = int(pt_mtd.cell(2, 2).value)
    mtd_alexsamm = int(pt_mtd.cell(2, 3).value)
    mtd_andy = int(pt_mtd.cell(2, 4).value)
    mtd_mario = int(pt_mtd.cell(2, 5).value)
    mtd_anfernnie = int(pt_mtd.cell(2, 6).value)
    mtd_daejon = int(pt_mtd.cell(2, 7).value)
    mtd_jose = int(pt_mtd.cell(2, 8).value)
    mtd_david = int(pt_mtd.cell(2, 9).value)
    mtd_marco = int(pt_mtd.cell(2, 10).value)

    cds = ["Tony", "Luis", "Alex", "Andy", "Mario", "Anfernnie", "Daejon", "Jose"]
    adv = ["David EVO", "David REVO", "Marco EVO", "Marco REVO"]

    imageLOGO = Image.open(urlopen("https://i.ibb.co/WGjVK32/logopng.png"))
    st.image(imageLOGO)

    # Hide 'Made with Streamlit' & app menu
    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    st.title("Packaging Team Metrics")
    st.write("---")

    # Sidebar
    st.sidebar.header(f"Welcome {name}")
    authenticator.logout("Signout", "sidebar")
    cds_team = st.sidebar.multiselect("Select CDS team member: ", cds)
    adv_team = st.sidebar.multiselect("Select Advantage team member: ", adv)

    # MTD
    mtd_ind = {
        "Tony": i_tony,
        "Luis": i_luis,
        "Alex": i_alexsamm,
        "Andy": i_andy,
        "Mario": i_mario,
        "Anfernnie": i_anfernnie,
        "Daejon": i_daejon,
        "Jose": i_jose,
    }
    mtd_bulk = {
        "Tony": b_tony,
        "Luis": b_luis,
        "Alex": b_alexsamm,
        "Andy": b_andy,
        "Mario": b_mario,
        "Anfernnie": b_anfernnie,
        "Daejon": b_daejon,
        "Jose": b_jose,
    }
    mtd_adv = {"David": mtd_david, "Marco": mtd_marco}

    mtd_mtd = {
        "Tony": mtd_tony,
        "Luis": mtd_luis,
        "Alex": mtd_alexsamm,
        "Andy": mtd_andy,
        "Mario": mtd_mario,
        "Anfernnie": mtd_anfernnie,
        "Daejon": mtd_daejon,
        "Jose": mtd_jose,
        "David": mtd_david,
        "Marco": mtd_marco,
    }

    max_ind = max(mtd_ind, key=mtd_ind.get)
    max_bulk = max(mtd_bulk, key=mtd_bulk.get)
    max_adv = max(mtd_adv, key=mtd_adv.get)
    max_mtd = max(mtd_mtd, key=mtd_mtd.get)

    st.subheader("Top Packagers")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Top Packager", f"{str(max_mtd)}: {str(mtd_mtd[max_mtd])}")
    col2.metric("Individual Packaging", f"{str(max_ind)}: {str(mtd_ind[max_ind])}")
    col3.metric("Bulk Packaging", f"{str(max_bulk)}: {str(mtd_bulk[max_bulk])}")
    col4.metric("Advantage Packaging", f"{str(max_adv)}: {str(mtd_adv[max_adv])}")

    # tabs
    tab1, tab2, tab3 = st.tabs(
        ["Individual Packaging", "Bulk Packaging", "Advantage Packaging"]
    )

    tab1.subheader("Chart")
    tab1.subheader("")
    tab1.line_chart(individual, x="Date", y=cds_team)
    tab1.subheader("")
    tab1.write("---")
    tab1.subheader("Data")
    tab1.table(data=individual)
    tab1.subheader("")
    tab1.write("---")
    tab1.subheader("Individual Total")
    tab1.code(f"Tony: {i_tony}")
    tab1.code(f"Luis: {i_luis}")
    tab1.code(f"Alex: {i_alexsamm}")
    tab1.code(f"Andy: {i_andy}")
    tab1.code(f"Mario: {i_mario}")
    tab1.code(f"Anfernnie: {i_anfernnie}")
    tab1.code(f"DaeJon: {i_daejon}")
    tab1.code(f"Jose: {i_jose}")

    tab2.subheader("Chart")
    tab2.subheader("")
    tab2.line_chart(bulk, x="Date", y=cds_team)
    tab2.subheader("")
    tab2.write("---")
    tab2.subheader("Data")
    tab2.table(data=bulk)
    tab2.subheader("")
    tab2.write("---")
    tab2.subheader("Bulk Total")
    tab2.code(f"Tony: {b_tony}")
    tab2.code(f"Luis: {b_luis}")
    tab2.code(f"Alex: {b_alexsamm}")
    tab2.code(f"Andy: {b_andy}")
    tab2.code(f"Mario: {b_mario}")
    tab2.code(f"Anfernnie: {b_anfernnie}")
    tab2.code(f"DaeJon: {b_daejon}")
    tab2.code(f"Jose: {b_jose}")

    tab3.subheader("Chart")
    tab3.subheader("")
    tab3.line_chart(advantage, x="Date", y=adv_team)
    tab3.subheader("")
    tab3.write("---")
    tab3.subheader("Data")
    tab3.table(data=advantage)
    tab3.subheader("")
    tab3.write("---")
    tab3.subheader("Advantage Total")
    tab3.code(f"David EVO: {david_evo}")
    tab3.code(f"David REVO: {david_revo}")
    tab3.code(f"Marco EVO: {marco_evo}")
    tab3.code(f"Marco REVO: {marco_revo}")

if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    st.warning("Please enter your username and password")
