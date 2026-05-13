import streamlit as st

st.set_page_config(page_title="GSA UI Sandbox", layout="wide")

st.write("Aktuelle Primärfarbe:", st.config.get_option("theme.primaryColor"))

# Sidebar Design
with st.sidebar:
    st.title("GSA Prototyp")
    st.divider()
    st.header("Konfiguration")
    liga = st.selectbox("Liga", ["Bundesliga", "Premier League", "La Liga"])
    st.success(f"Ausgewählt: {liga}")

# Hauptbereich
st.title("Willkommen im UI-Labor")
st.write("Hier entstehen die Komponenten für den GenSoccerAnalyzer.")