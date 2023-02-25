import pandas as pd
import numpy as np
import gspread
import streamlit as st
import ssl
from PIL import Image
from urllib.request import urlopen
import pickle
import streamlit_authenticator as stauth
from pathlib import Path
from datetime import datetime
from datetime import date
import datetime

ssl._create_default_https_context = ssl._create_unverified_context

try:

    class QA_Tracker:
        def __init__(self):
            self.st = st
            self.start_dateTime = date(2022, 12, 1)
            self.today = datetime.datetime.now()
            self.current_month = self.today.month
            self.current_year = self.today.year

            self.st.set_page_config(layout="wide")
            self.hide_streamlit_style = """
                    <style>
                    #MainMenu {visibility: hidden;}
                    footer {visibility: hidden;}
                    </style>
                    """
            self.st.markdown(self.hide_streamlit_style, unsafe_allow_html=True)
            self.names = ["Paul Vergara", "Jesus Lopez", "Kristen Hale", "Josh Santana"]
            self.usernames = ["pvergara", "jlopez", "khale", "jsantana"]
            self.file_path = Path(__file__).parent / "hashed_pw.pkl"
            self.credentials = {"usernames": {}}
            self.authenticator = stauth.Authenticate(
                self.credentials, "cds_pack", "guW70qH9RX", cookie_expiry_days=30
            )

        def load_data(self):
            with self.file_path.open("rb") as file:
                self.hashed_passwords = pickle.load(file)
            for uname, name, pwd in zip(
                self.usernames, self.names, self.hashed_passwords
            ):
                user_dict = {"name": name, "password": pwd}
                self.credentials["usernames"].update({uname: user_dict})

        def authenticate(self):
            (
                self.name,
                self.authentication_status,
                self.username,
            ) = self.authenticator.login("Login", "main")

        def access_spreadsheet(self):
            if self.authentication_status:
                self.scope = [
                    "https://spreadsheets.google.com/feeds",
                    "https://www.googleapis.com/auth/drive",
                ]
                client = gspread.service_account(filename="service_account.json")
                self.database = client.open("Database")
                self.device_management_arrow = self.database.worksheet("arrow_qa")
                self.device_management_dagger = self.database.worksheet("dagger_qa")
                self.arrow_qa = pd.DataFrame(
                    self.device_management_arrow.get_all_records()
                )
                self.dagger_qa = pd.DataFrame(
                    self.device_management_dagger.get_all_records()
                )

        def process_data(self):
            self.arrow_passed_qty = self.arrow_qa["Quantity"]
            self.dagger_passed_qty = self.dagger_qa["Quantity"]
            self.arrow_qa["Date"] = pd.to_datetime(self.arrow_qa["Date"])
            self.dagger_qa["Date"] = pd.to_datetime(self.dagger_qa["Date"])
            self.arrow_qa = self.arrow_qa.sort_values(by="Date")
            self.dagger_qa = self.dagger_qa.sort_values(by="Date")
            self.dates_passed_arrow = self.arrow_qa["Date"]
            self.dates_passed_dagger = self.dagger_qa["Date"]
            self.arrow_passed_average = int(np.mean(self.arrow_qa["Quantity"]))
            self.dagger_passed_average = int(np.mean(self.dagger_qa["Quantity"]))
            self.monthtodate_arrow = self.arrow_qa[
                (self.dates_passed_arrow.dt.month == self.current_month)
                & (self.dates_passed_arrow.dt.year == self.current_year)
            ]
            self.monthtodate_dagger = self.dagger_qa[
                (self.dates_passed_dagger.dt.month == self.current_month)
                & (self.dates_passed_dagger.dt.year == self.current_year)
            ]
            self.monthtodate_arrow["Date"] = self.monthtodate_arrow["Date"].dt.strftime(
                "%Y-%m-%d"
            )
            self.monthtodate_dagger["Date"] = self.monthtodate_dagger[
                "Date"
            ].dt.strftime("%Y-%m-%d")
            self.mtd_arrow = self.monthtodate_arrow["Quantity"]
            self.mtd_dagger = self.monthtodate_dagger["Quantity"]

            self.ytd_arrow = self.arrow_qa[
                self.dates_passed_arrow.dt.year == self.current_year
            ]
            self.ytd_dagger = self.dagger_qa[
                self.dates_passed_dagger.dt.year == self.current_year
            ]
            self.ytd_arrow_qty = self.ytd_arrow["Quantity"]
            self.ytd_dagger_qty = self.ytd_dagger["Quantity"]
            self.ytd_arrow_average = int(np.mean(self.ytd_arrow_qty))
            self.ytd_dagger_average = int(np.mean(self.ytd_dagger_qty))

        def display_data(self):
            self.imageLOGO = Image.open(urlopen("https://i.ibb.co/WGjVK32/logopng.png"))
            st.image(self.imageLOGO)
            st.title("QA Tracker")

            st.markdown("---")
            st.write("--- SUMMARY ---")

            col1, col2, col3, col4 = st.columns(4)
            col1.metric(
                "Average daily QA'd devices (Arrow): ", self.arrow_passed_average
            )
            col2.metric(
                "Average daily QA'd devices (Dagger): ", self.dagger_passed_average
            )
            col3.metric(
                "Year to date average QA'd devices (Arrow): ", self.ytd_arrow_average
            )
            col4.metric(
                "Year to date average QA'd devices (Dagger): ", self.ytd_dagger_average
            )

            col5, col6, col7, col8 = st.columns(4)
            col5.metric("Month to date QA'd devices (Arrow): ", self.mtd_arrow.sum())
            col6.metric("Month to date QA'd devices (Dagger): ", self.mtd_dagger.sum())
            col7.metric("Year to date QA'd devices (Arrow): ", self.ytd_arrow_qty.sum())
            col8.metric(
                "Year to date QA'd devices (Dagger): ", self.ytd_dagger_qty.sum()
            )

            tab1, tab2 = st.tabs(["Arrow", "Dagger"])

            with tab1:
                st.markdown("--- **ARROW** ---")
                st.write("Line Chart")
                st.line_chart(
                    self.arrow_qa, x="Date", y="Quantity", width=150, height=300
                )
                st.write("Month-to-Date Bar Chart")
                st.bar_chart(
                    self.monthtodate_arrow,
                    x="Date",
                    y="Quantity",
                    width=150,
                    height=300,
                )
                st.dataframe(self.monthtodate_arrow)
            with tab2:
                st.markdown("--- **DAGGER** ---")
                st.write("Line Chart")
                st.line_chart(
                    self.dagger_qa, x="Date", y="Quantity", width=150, height=300
                )
                st.write("Month to Date Bar Chart")
                st.bar_chart(
                    self.monthtodate_dagger,
                    x="Date",
                    y="Quantity",
                    width=150,
                    height=300,
                )
                st.dataframe(self.monthtodate_dagger)

    if __name__ == "__main__":
        tracker = QA_Tracker()
        tracker.load_data()
        tracker.authenticate()
        tracker.access_spreadsheet()
        tracker.process_data()
        tracker.display_data()

except (AttributeError, NameError):
    pass
