import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="EV Fleet Dashboard")

st.title("🚗 EV Fleet Health Dashboard")

df = pd.DataFrame(requests.get("http://127.0.0.1:8000/vehicles").json())

if len(df):

    st.dataframe(df)

    st.subheader("Latest Battery Health")

    st.bar_chart(df.set_index("vehicle_id")["soh"])

    st.subheader("Temperature")

    st.line_chart(df["temperature"])

    st.subheader("Alerts")

    alerts = df[df["soh"] < 75]

    st.dataframe(alerts)

else:

    st.write("No data yet.")