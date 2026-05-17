import streamlit as st

# Globale Konfiguration für die gesamte App (mit deinem SVG-Logo)
st.set_page_config(page_title="GenSoccerAnalyzer", page_icon="⚽",layout="wide")

# --- NEUER BEREICH: WILLKOMMEN & PROJEKT-ÜBERSICHT ---
st.title("⚽ GenSoccerAnalyzer (GSA)")
st.subheader("Willkommen beim KI-gestützten Fußball-Analysten")

st.markdown("""
Dieses System kombiniert klassische NLP-Methoden mit modernster Agentic AI und RAG, 
um tiefe Einblicke in europäische Top-Ligen zu gewähren.

### 🎉 Projekt-Übersicht:
- **📊 Statistiken & EDA:** Analyse strukturierter StatsBomb-Daten.
- **🔍 Wikipedia Clustering:** Unüberwachtes Lernen über Vereinsphilosophien.
- **🤖 GSA AI Chat:** Das Multi-Agenten-System für komplexe, deutschsprachige Abfragen.

*Nutzen Sie die Seitenleiste links oder den 'pages'-Ordner, um zwischen den Modulen zu wechseln.*
""")

st.divider() # Trennlinie zum technischen Test-Bereich

st.write("Aktuelle Primärfarbe:", st.config.get_option("theme.primaryColor"))

# Zugriff auf die Secrets
geheimnis = st.secrets.get("FAVORITE_TEAM", "Kein Team gefunden")

# Sidebar Design & Konfiguration
with st.sidebar:
    st.title("GSA Prototyp")
    st.divider()
    
    # Dein bestehender Info-Kasten für den Agenten
    st.sidebar.info(f"KI-Agent konfiguriert für: {geheimnis}")
    st.divider()
    
    st.header("Konfiguration")
    liga = st.selectbox("Liga", ["Bundesliga", "Premier League", "La Liga"])
    st.success(f"Ausgewählt: {liga}")

