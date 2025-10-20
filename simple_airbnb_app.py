
import streamlit as st
import pandas as pd

# --- Beispiel-Daten erstellen ---
data = {
    "id": [101, 102, 103, 104],
    "name": ["Cozy Loft", "Modern Studio", "Beach Apartment", "City Flat"],
    "city": ["Berlin", "Hamburg", "Berlin", "Munich"],
    "price_per_night": [75, 90, 120, 80]
}

df = pd.DataFrame(data)

# --- Titel ---
st.title("🏠 Simple Airbnb App")

# --- Filterfeld ---
city = st.text_input("Enter city name (e.g. Berlin):").title()

# --- Filter anwenden ---
if city:
    filtered = df[df["city"] == city]
    if not filtered.empty:
        st.dataframe(filtered)
    else:
        st.warning("No apartments found for this city.")
else:
    st.info("Please enter a city name above.")

# --- Gesamtdaten optional anzeigen ---
if st.checkbox("Show all data"):
    st.dataframe(df)
