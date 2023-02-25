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
    imageLOGO = Image.open(urlopen("https://i.ibb.co/WGjVK32/logopng.png"))
    st.image(imageLOGO)

    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    st.sidebar.header(f"Welcome {name}")
    authenticator.logout("Signout", "sidebar")
    product_codes = [
        "4-6341-20",
        "4-6340-20",
        "4-6341-10",
        "4-6340-10",
        "4-6350-17",
        "4-6351-17",
        "4-8470-20",
        "4-8470-10",
        "Arrow-L",
        "4-6201-10",
    ]
    selected_code = st.sidebar.selectbox("Select a device:", product_codes)

    if selected_code == "4-6341-20":
        st.header("ArrowGVI - AerisPro - Non-CAN")

        st.subheader("103")
        st.markdown("Upload")
        st.code("4-6341-20")

        st.markdown("---")
        st.subheader("115")
        st.markdown("Tracker / QA Script")
        st.code(
            """
    Product Code: 4-6341-520
Config: 772
    """
        )
        st.write("")

        st.markdown("NetSuite Sales Kits")
        st.code(
            """
    8-6341-520 - ArrowVI - Gemtek AerisPro without VIN - 5-wire Harness
8-6343-520 - ArrowVI - Gemtek AerisPro without VIN - OBD Harness (3-2009)
8-6345-520 - ArrowVI - Gemtek AerisPro without VIN - Universal Domestic Harness
8-6347-520 - ArrowVI - Gemtek AerisPro without VIN - Universal Import Harness
8-6331-520 - ArrowVI - Gemtek AerisPro without VIN - Honda Harness
8-6349-520 - ArrowVI - Gemtek AerisPro without VIN - Device Only
        """
        )

        st.markdown("---")
        st.subheader("102")
        st.markdown("Tracker / QA Script")
        st.code(
            """
    4-6341-220 - ArrowVI - Gemtek without CAN
- With 5-wire Harness / Config 384
- With Buzzer Harness - 341
    """
        )

        st.markdown("NetSuite Sales Kits")
        st.code(
            """
1-6341-220 - EvoVI with 5 wire Harness (without CAN)
1-6344-220 - EvoVI with Buzzer Harness (without CAN)
        """
        )

        st.markdown("---")
        st.subheader("108")
        st.markdown("Tracker / QA Script")
        st.code(
            """
    4-6341-820 - ArrowVI - Gemtek without CAN
- With 5-wire Harness - Config 330
    
    """
        )

        st.markdown("NetSuite Sales Kits")
        st.code(
            """
1-6541-820 - Ryken Powered with 5 wire Harness (without CAN)
        """
        )

    elif selected_code == "4-6340-20":
        st.header("ArrowGVI - AerisPro - CAN")

        st.subheader("103")
        st.markdown("Upload")
        st.code("4-6340-20")

        st.markdown("---")
        st.subheader("115")
        st.markdown("Tracker / QA Script")
        st.code(
            """
Product Code: 4-6340-520
Config: 771
    """
        )
        st.write("")

        st.markdown("NetSuite Sales Kits")
        st.code(
            """
    8-6340-520 - ArrowVI - Gemtek AerisPro without VIN - 5-wire Harness
8-6342-520 - ArrowVI - Gemtek AerisPro with VIN - OBD Harness (3-2033)
8-6344-520 - ArrowVI - Gemtek AerisPro with VIN - Universal Domestic Harness
8-6346-520 - ArrowVI - Gemtek AerisPro with VIN - Universal Import Harness
8-6330-520 - ArrowVI - Gemtek AerisPro with VIN - Honda Harness
8-6348-520 - ArrowVI - Gemtek AerisPro with VIN - Device Only
        """
        )

        st.markdown("---")
        st.subheader("102")
        st.markdown("Tracker / QA Script")
        st.code(
            """
    4-6340-220 - ArrowVI - Gemtek with CAN
- With 5-wire Harness - Config 381
- With VinVerify - Config 382
- With Buzzer Harness - Config 383
    """
        )

        st.markdown("NetSuite Sales Kits")
        st.code(
            """
    1-6340-220 - Arrow 6 Gemtek w CAN w 5-wire Harness AP
1-6343-220 - Arrow 6 Gemtek w CAN/Buzzer Harness AP
1-6342-220 - ArrowVI Gemtek VV - AP
        """
        )

        st.markdown("---")
        st.subheader("108")
        st.markdown("Tracker / QA Script")
        st.code(
            """
    4-6340-820 - ArrowVI - Gemtek with CAN
- With 5-wire Harness - Config 330
    """
        )

        st.markdown("NetSuite Sales Kits")
        st.code(
            """
1-6540-820 - Ryken Powered Gemtek with 5 wire Harness - AerisPro
        """
        )

    elif selected_code == "4-6341-10":
        st.header("ArrowGVI - T-Mobile - Non-CAN")

        st.subheader("103")
        st.markdown("Upload")
        st.code("4-6341-10")

        st.markdown("---")
        st.subheader("115")
        st.markdown("Tracker / QA Script")
        st.code(
            """
Product Code: 4-6341-10
Config: 316
    """
        )
        st.write("")

        st.markdown("NetSuite Sales Kits")
        st.code(
            """
    8-6341-10 - ArrowGVI - T-Mobile without CAN - 5-wire Harness
8-6343-10 - ArrowGVI - T-Mobile without CAN - OBD Harness (3-2009)
8-6345-10 - ArrowGVI - T-Mobile without CAN - Universal Domestic Harness
8-6347-10 - ArrowGVI - T-Mobile without CAN - Universal Import Harness
8-6349-10 - ArrowGVI - T-Mobile without CAN - Device Only
    """
        )

        st.markdown("---")
        st.subheader("102")
        st.markdown("Tracker / QA Script")
        st.code(
            """
    4-6341-10 - ArrowVI - Gemtek without CAN
- With 5-wire Harness - Config 341
    """
        )

        st.markdown("NetSuite Sales Kits")
        st.code(
            """
    1-6341-10 - EvoVI Gemtek with 5 wire Harness - T-Mobile
1-6347-10 - EvoVI Gemtek - Device Only
        """
        )

        st.markdown("---")
        st.subheader("108")
        st.markdown("Tracker / QA Script")
        st.code(
            """
    4-6341-10 - ArrowVI - Gemtek without CAN
- With 5-wire Harness - Config 312
    """
        )

        st.markdown("NetSuite Sales Kits")
        st.code(
            """
1-6541-10 - EvoTrackVI Gemtek with 5 wire Harness - T-Mobile
        """
        )

    elif selected_code == "4-6340-10":
        st.header("ArrowGVI - T-Mobile - CAN")

        st.subheader("103")
        st.markdown("Upload")
        st.code("4-6340-10")

        st.markdown("---")
        st.subheader("115")
        st.markdown("Tracker / QA Script")
        st.code(
            """
Product Code: 4-6340-10
Config: 314
    """
        )
        st.write("")

        st.markdown("NetSuite Sales Kits")
        st.code(
            """
    8-6340-10 - ArrowGVI - T-Mobile with CAN - 5-wire Harness
8-6342-10 - ArrowGVI - T-Mobile with CAN - OBD Harness (3-2033)
8-6344-10 - ArrowGVI - T-Mobile with CAN - Universal Domestic Harness
8-6346-10 - ArrowGVI - T-Mobile with CAN - Universal Import Harness
8-6348-10 - ArrowGVI - T-Mobile with CAN - Device Only
    """
        )

        st.markdown("---")
        st.subheader("102")
        st.markdown("Tracker / QA Script")
        st.code(
            """
    4-6340-10 - ArrowVI - Gemtek with CAN
- With 5-Wire Harness - Config 342
- With VIN-Verify Harness - Config 369
- With Buzzer Harness - 348
    """
        )

        st.markdown("NetSuite Sales Kits")
        st.code(
            """
    1-6340-10 - EvoVI Gemtek with 5 wire Harness - T-Mobile
1-6342-10 - ArrowVI Gemtek VV - TMobile
1-6343-10 - Arrow 6 Gemtek w CAN/Buzzer Harness TM
1-6347-10 - EvoVI Gemtek - Device Only - T-Mobile
        """
        )

        st.markdown("---")
        st.subheader("108")
        st.markdown("Tracker / QA Script")
        st.code(
            """
    4-6340-10 - ArrowVI - Gemtek with CAN
- With 5-wire Harness - Config 310
    """
        )

        st.markdown("NetSuite Sales Kits")
        st.code(
            """
1-6540-10 - EvoVI Gemtek with 5 wire Harness - T-Mobile
        """
        )

    elif selected_code == "4-6350-17":
        st.header("ArrowHQ - Verizon - CAN")

        st.subheader("103")
        st.markdown("Upload")
        st.code("4-6350-17")

        st.markdown("---")
        st.subheader("115")
        st.markdown("Tracker / QA Script")
        st.code(
            """
Product Code: 4-6350-17
Config: 313
    """
        )
        st.write("")

        st.markdown("NetSuite Sales Kits")
        st.code(
            """
    8-6350-17 - ArrowHQ - Verizon with CAN - 5-wire Harness
8-6352-17 - ArrowHQ - Verizon with CAN - OBD Harness (3-2033)
8-6354-17 - ArrowHQ - Verizon with CAN - Universal Domestic
8-6356-17 - ArrowHQ - Verizon with CAN - Universal Import
8-6332-17 - ArrowHQ - Verizon with CAN - Honda
8-6358-17 - ArrowHQ - Verizon with CAN - Device Only
    """
        )

        st.markdown("---")
        st.subheader("102")
        st.markdown("Tracker / QA Script")
        st.code(
            """
    4-6350-17 - ArrowHQ - with CAN
- With 5-Wire Harness - Config 338
- With Buzzer Harness - Config 349
    """
        )

        st.markdown("NetSuite Sales Kits")
        st.code(
            """
    1-6350-17 - EvoQH with CAN with 5 wire Harness - Verizon
1-6352-17 - EvoQH with CAN with OBD Harness - Verizon
1-6353-17 - EvoQH with CAN with CAN with Buzzer - Verizon
1-6358-17 - EvoQH with CAN - Device Only - Verizon
        """
        )

        st.markdown("---")
        st.subheader("108")
        st.markdown("Tracker / QA Script")
        st.code(
            """
    4-6350-17 - ArrowHQ - with CAN
- With 5-wire Harness - Config 315
    """
        )

        st.markdown("NetSuite Sales Kits")
        st.code(
            """
1-6550-17 - RykenpoweredQH with 5 wire Harness - Verizon
        """
        )

    elif selected_code == "4-6351-17":
        st.header("ArrowHQ - Verizon - without CAN")

        st.subheader("103")
        st.markdown("Upload")
        st.code("4-6351-17")

        st.markdown("---")
        st.subheader("115")
        st.markdown("Tracker / QA Script")
        st.code(
            """
Product Code: 4-6351-17
Config: 320
    """
        )
        st.write("")

        st.markdown("NetSuite Sales Kits")
        st.code(
            """
    8-6351-17 - ArrowHQ - Verizon without CAN - 5-wire Harness
8-6333-17 - ArrowHQ - Verizon without CAN - Honda
8-6353-17 - ArrowHQ - Verizon without CAN - OBD Harness (3-2009)
8-6355-17 - ArrowHQ - Verizon without CAN - Universal Domestic
8-6357-17 - ArrowHQ - Verizon without CAN - Universal Import
8-6359-17 - ArrowHQ - Verizon without CAN - Device Only
    """
        )

        st.markdown("---")
        st.subheader("102")
        st.markdown("Tracker / QA Script")
        st.code(
            """
    4-6351-17 - ArrowHQ - without CAN
- With 5-Wire Harness - Config 340
- With Device Only - Config 340
    """
        )

        st.markdown("NetSuite Sales Kits")
        st.code(
            """
    1-6351-17 - EvoVI with 5 wire Harness - Verizon
1-6359-17 - EvoVI - Device Only - Verizon
        """
        )

        st.markdown("---")
        st.subheader("108")
        st.markdown("Tracker / QA Script")
        st.code(
            """
    4-6351-17 - ArrowHQ - without CAN
- With 5-wire Harness - Config 317
    """
        )

        st.markdown("NetSuite Sales Kits")
        st.code(
            """
1-6551-17 - EvoTrackVI with 5 wire Harness - Verizon
        """
        )

    elif selected_code == "4-8470-20":
        st.header("Dagger QG Slim - AP")

        st.subheader("103")
        st.markdown("Upload")
        st.code("4-8470-20")

        st.write("")

        st.markdown("---")
        st.subheader("102")
        st.markdown("Tracker / QA Script")
        st.code(
            """
    Product Code: 4-8502-220

REVO ONE - Config 387
REVO SmartStop-3K - Config 388
REVO 3000 - Config 389
REVO 4000 - Config 390
REVO 5000 - Config 391
REVO SmartStop-5K - Config 395
    """
        )

        st.markdown("NetSuite Sales Kits")
        st.code(
            """
    REVO ONE - 1-8411-220-1012
Revo SmartStop-3K - 1-8421-220-1018
Revo SmartStop-5K - 1-8423-210-1036
Revo 3000 - 1-8431-220-1042
Revo 4000 - 1-8441-220-1054
Revo 5000 - 1-8451-220-1066

        """
        )

        st.markdown("---")
        st.subheader("108")
        st.markdown("Tracker / QA Script")
        st.code(
            """
    Product Code: 4-8502-820

REVO SmartStop - Config 326
REVO 3000 - Config 327
REVO 4000 - Config 328
REVO 5000 - Config 329
    """
        )

        st.markdown("NetSuite Sales Kits")
        st.code(
            """
Revo SmartStop - 1-8421-820-1018
Revo 3000 - 1-8431-820-1042
Revo 4000 - 1-8441-820-1054
Revo 5000 - 1-8451-820-1066    
        """
        )

    elif selected_code == "4-8470-10":
        st.header("Dagger QG Slim - T-Mobile")

        st.subheader("103")
        st.markdown("Upload")
        st.code("4-8470-10")

        st.write("")

        st.markdown("---")
        st.subheader("102")
        st.markdown("Tracker / QA Script")
        st.code(
            """
    Product Code: 4-8502-210

REVO ONE - Config 351
REVO SmartStop-3K - Config 354
REVO 3000 - Config 357
REVO 4000 - Config 360
REVO 5000 - Config 363
REVO SmartStop-5K - Config 394
    """
        )

        st.markdown("NetSuite Sales Kits")
        st.code(
            """
    REVO ONE - 1-8411-210
REVO SmartStop-3K - 1-8421-210
REVO 3000 - 1-8431-210
REVO 4000 - 1-8441-210
REVO 5000 - 1-8451-210
REVO SmartStop-5K - 1-8423-210
        """
        )

        st.markdown("---")
        st.subheader("108")
        st.markdown("Tracker / QA Script")
        st.code(
            """
    Product Code: 4-8502-810

REVO SmartStop - Config 320
REVO 3000 - Config 321
REVO 4000 - Config 322
REVO 5000 - Config 323
    """
        )

        st.markdown("NetSuite Sales Kits")
        st.code(
            """
RevoTrack 3.0 - SmartStop - 1-8421-810
RevoTrack 3.0 - 3000 - 1-8431-810
RevoTrack 3.0 - 4000 - 1-8441-810
RevoTrack 3.0 - 5000  - 1-8451-810  
        """
        )

    elif selected_code == "Arrow-L":
        st.header("Arrow-L")

        st.subheader("103")
        st.markdown("Upload")
        st.code("4-6510-10")

        st.markdown("---")
        st.subheader("109")
        st.markdown("Tracker / QA Script")
        st.code(
            """
Product Code: 4-1005-10
Config: 299
    """
        )
        st.write("")

        st.markdown("NetSuite Sales Kits")
        st.code(
            """
Remote Start Kit - 3 Year: 8-ARLX11-TO-3Y-MC
Remote Start Kit - 1 Year: 8-ARLX11-TO-1Y-MC
Device Only - 3 Year - 8-ARLX11-M-1
Device Only - 1 Year - 8-ARLX11-M-3
    """
        )

    elif selected_code == "4-6201-10":
        st.header("ArrowHQ - Verizon - CAN")

        st.subheader("103")
        st.markdown("Upload")
        st.code("4-6201-10")

        st.markdown("---")
        st.subheader("115")
        st.markdown("Tracker / QA Script")
        st.code(
            """
    Product Code: 4-7322-10
Config: 321
    """
        )
        st.write("")

        st.markdown("NetSuite Sales Kits")
        st.code(
            """
    8-7322-10 - ArrowGVI-67 (DO)
8-7323-10 - ArrowGVI-67 with Harley Harness - Harness included is the 3-2044
    """
        )

        st.markdown("---")
        st.subheader("102")
        st.markdown("Tracker / QA Script")
        st.code(
            """
    Product Code: 4-6360-10
Config: 360
    """
        )

        st.markdown("NetSuite Sales Kits")
        st.code(
            """
    1-6360-10 - Evo-WR with Harness (EVO Water Resistant)
1-6369-10-1001 - EvoWR (DO)
        """
        )

        st.markdown("---")
        st.subheader("108")
        st.markdown("Tracker / QA Script")
        st.code(
            """
Product Code: 4-6360-10
Config: 318
    """
        )

        st.markdown("NetSuite Sales Kits")
        st.code(
            """
1-6360-810 - EvoTrack-WR
1-6369-810-1001 - EvoTrack-WR (DO)
        """
        )

if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    st.warning("Please enter your username and password")
