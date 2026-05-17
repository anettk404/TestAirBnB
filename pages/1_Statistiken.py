# pages/1_Statistiken.py

import streamlit as st
import pandas as pd

st.title("📊 Statistiken & EDA")
st.write("Hier finden Sie die quantitativen Analysen basierend auf den StatsBomb-Daten.")

# Beispiel für interaktiven Filter (wird später mit echten Daten befüllt)
liga = st.selectbox("Wähle eine Liga:", ["Bundesliga", "Premier League", "La Liga"])

st.info(f"Hier entstehen bald die Barcharts und KPIs für die {liga}.")

# Dummy-Diagramm zur Veranschaulichung
chart_data = pd.DataFrame({"Tore": [23, 17, 35]}, index=["Team A", "Team B", "Team C"])
st.bar_chart(chart_data)