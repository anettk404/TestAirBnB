import streamlit as st
import pandas as pd

# Globale Konfiguration
st.set_page_config(
    page_title="GenSoccerAnalyzer",
    page_icon="openclipart-vectors-football-157930.svg",
    layout="wide"
)

# --- GLOBALE SIDEBAR (Gleich für alle Tabs) ---
with st.sidebar:
    st.title("⚽ GSA Prototyp")
    st.divider()
    st.header("Filter & Konfiguration")
    
    # Eure Filter aus den Mockups
    liga = st.selectbox("Liga", ["Bundesliga", "Premier League", "La Liga", "Serie A", "Ligue 1"])
    saison = st.selectbox("Saison", ["2025/2026", "2024/2025"])
    team = st.selectbox("Team", ["Bayer Leverkusen", "Bayern München", "VfB Stuttgart", "Dortmund"])
    spieler = st.selectbox("Spieler", ["Florian Wirtz", "Harry Kane", "Jamal Musiala"])
    
    st.divider()
    # Zugriff auf die Moodle-Secrets (falls benötigt)
    geheimnis = st.secrets.get("FAVORITE_TEAM", "Kein Team hinterlegt")
    st.info(f"KI-Kontext aktiv für: {geheimnis}")

# --- HAUPTBEREICH: TITEL & DIE DREI REITER (TABS) ---
st.title("GenSoccerAnalyzer (GSA)")

# Hier erstellen wir die drei Reiter oben im Bild
tab_stats, tab_clustering, tab_chat = st.tabs([
    "📊 Statistiken & EDA", 
    "🔍 Wikipedia Clustering", 
    "🤖 GSA AI Chat"
])

# ==========================================
# 1. TAB: STATISTIKEN & EDA
# ==========================================
with tab_stats:
    st.header(f"Statistische Analyse: {spieler}")
    st.subheader(f"Aktuelle Leistungsdaten ({team} | Saison {saison})")
    
    # Layout aufteilen (z.B. für KPIs links und Charts rechts)
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.metric(label="Tore pro 90 Min (xG)", value="0.84", delta="+0.12")
        st.metric(label="Passquote", value="89.3%", delta="-1.2%")
        st.metric(label="Erfolgreiche Dribblings", value="64%", delta="+4.5%")
        
    with col2:
        st.write("Vergleich zum Ligadurchschnitt:")
        # Dummy-Dataframe für ein schickes Barchart
        chart_data = pd.DataFrame(
            {"Spieler": [0.84, 89.3, 64], "Liga-Schnitt": [0.32, 78.5, 42]},
            index=["Tore/90", "Pass%", "Dribbling%"]
        )
        st.bar_chart(chart_data)

# ==========================================
# 2. TAB: WIKIPEDIA CLUSTERING
# ==========================================
with tab_clustering:
    st.header("Document Clustering der europäischen Top-Ligen")
    st.write(f"Auswertung basierend auf Wikipedia-Stand: **Mai 2026** für die {liga}.")
    
    # Zwei Spalten: Links die Cluster-Auswahl/Infos, rechts die interaktive Grafik
    col_left, col_right = st.columns([1, 2])
    
    with col_left:
        cluster_id = st.slider("Wähle ein Cluster zum Inspizieren:", 0, 4, 2)
        st.markdown(f"### 📋 Details zu Cluster {cluster_id}")
        
        # Dynamische Keywords je nach Slider
        keywords = {
            0: "Abstiegskampf, Trainerwechsel, Defensivfokus",
            1: "Traditionsverein, hohe Mitgliederzahl, Mittelfeld",
            2: "Ballbesitz, Pressing, Internationale Klasse, Meisterschaft",
            3: "Investorenclub, hoher Transferumsatz, Talententwicklung",
            4: "Aufsteiger, Sensation, Kompakt"
        }
        st.info(f"**Top-Keywords:** {keywords[cluster_id]}")
        st.write(f"In diesem Cluster befinden sich aktuell u.a.: *{team}*")
        
    with col_right:
        st.write("### Interaktive t-SNE / PCA Visualisierung")
        # Hier kommt später euer echtes Plotly-Scatterplot rein
        st.warning("Hier wird das interaktive Scatter-Plot-Diagramm (z.B. mit Plotly) gerendert, bei dem jeder Punkt ein Verein ist.")

# ==========================================
# 3. TAB: GSA AI CHAT
# ==========================================
with tab_chat:
    st.header("🤖 GSA Multi-Agenten Chat")
    st.write(f"Kontextuelle Abfragen auf Deutsch für **{spieler}** ({team}).")
    
    # Chat-Historie im Session-State initialisieren
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Anzeigen der alten Nachrichten
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat-Eingabefeld am unteren Bildschirmrand des Tabs
    if user_query := st.chat_input("Frage die Agenten z.B.: Wie passt der Spielstil laut Wikipedia zu den Statsbomb-Daten?"):
        # Nutzer-Nachricht anzeigen & speichern
        with st.chat_message("user"):
            st.markdown(user_query)
        st.session_state.messages.append({"role": "user", "content": user_query})
        
        # Antwort simulieren (Später Verknüpfung mit CrewAI)
        with st.chat_message("assistant"):
            with st.spinner("Die Agenten (Stats, Wiki, Validator) analysieren den Kontext..."):
                st.markdown(f"**Antwort des GSA-Systems:** Basierend auf den Statsbomb-Daten der Saison {saison} und dem Wikipedia-Profil von *{spieler}* lässt sich sagen...")