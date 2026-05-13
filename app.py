import streamlit as st

st.set_page_config(page_title="GenSoccerAnalyzer", page_icon="⚽",layout="wide")

st.write("Aktuelle Primärfarbe:", st.config.get_option("theme.primaryColor"))

# Zugriff auf die Secrets
geheimnis = st.secrets.get("FAVORITE_TEAM", "Kein Team gefunden")

st.sidebar.info(f"KI-Agent konfiguriert für: {geheimnis}")



# Sidebar Design
with st.sidebar:
    st.title("GSA Prototyp")
    st.divider()
    st.header("Konfiguration")
    liga = st.selectbox("Liga", ["Bundesliga", "Premier League", "La Liga"])
    st.success(f"Ausgewählt: {liga}")

# Hauptbereich
st.title("Prototyp GenSoccerAnalyzer")
st.write("Hier entstehen die verschiedenen Komponenten.")