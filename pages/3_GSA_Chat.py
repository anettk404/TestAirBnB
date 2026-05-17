# pages/3_GSA_Chat.py
import streamlit as st

st.title("GSA AI Chatbot")
st.write("Stellen Sie Ihre Fragen zum europäischen Fußball auf Deutsch.")

# Konversations-Kontext initialisieren (Streamlit-Standard für Chats)
if "messages" not in st.session_state:
    st.session_state.messages = []

# Bisherige Chat-Historie anzeigen
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
if user_query := st.chat_input("z.B. Welcher Verein im Cluster 2 passt statistisch am besten zu Spieler X?"):
    with st.chat_message("user"):
        st.markdown(user_query)
    st.session_state.messages.append({"role": "user", "content": user_query})
    
    # Platzhalter für die CrewAI / RAG Antwort
    with st.chat_message("assistant"):
        with st.spinner("Die Agenten beratschlagen sich..."):
            # Später: crew.kickoff(inputs={"query": user_query})
            st.markdown(f"**Antwort des Validators:** (Hier wird die Antwort des Agenten-Systems ausgegeben).")