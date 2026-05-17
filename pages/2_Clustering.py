# pages/2_Clustering.py
import streamlit as st

st.title("🔍 Wikipedia Document Clustering")
st.write("Ergebnisse des Unsupervised Learnings über die Top-Vereine Europas (Stand: 05/2026).")

# Platzhalter für die interaktive Grafik (z.B. Plotly Scatter Plot)
st.subheader("Interaktive Cluster-Visualisierung")
st.warning("Hier wird die t-SNE / PCA Reduktion eurer Embeddings visualisiert.")

# Beispiel für Interaktivität laut Aufgabenstellung
selected_cluster = st.slider("Wähle ein Cluster zum Erkunden:", 0, 4)
st.write(f"Häufigste Keywords in Cluster {selected_cluster}: *Ballbesitz, Pressing, Umschaltspiel*")