
### Part 1: Import necessary packages ###
import streamlit as st
import pandas as pd
import plotly.express as px

### Part 2: Define helper functions ###
def load_data():
    url = "http://data.insideairbnb.com/germany/berlin/berlin/2025-09-05/visualisations/listings.csv"
    return pd.read_csv(url)

### Part 3: Define pages ###
def page_search(df):
    st.title("🏙️ Apartment Search")
    city = st.text_input("Stadt eingeben:")
    filtered = df[df["neighbourhood_cleansed"].str.contains(city, case=False, na=False)]
    st.dataframe(filtered[["id", "name", "price", "review_scores_rating"]])

def page_details(df):
    st.title("🏠 Apartment Details")
    apt_id = st.selectbox("Apartment-ID wählen", df["id"])
    apt = df[df["id"] == apt_id].iloc[0]
    st.write(f"**Name:** {apt['name']}")
    st.write(f"**Preis:** {apt['price']} €")
    st.write(f"**Bewertung:** {apt['review_scores_rating']} ⭐")

def page_compare(df):
    st.title("📊 Apartment Comparison")
    ids = st.multiselect("Apartments wählen", df["id"])
    if ids:
        subset = df[df["id"].isin(ids)]
        fig = px.bar(subset, x="name", y="price", title="Preise im Vergleich (€)")
        st.plotly_chart(fig)

### Part 4: Main program ###
df = load_data()
page = st.sidebar.selectbox("Seite wählen", ["Search", "Details", "Compare"])

if page == "Search":
    page_search(df)
elif page == "Details":
    page_details(df)
else:
    page_compare(df)

