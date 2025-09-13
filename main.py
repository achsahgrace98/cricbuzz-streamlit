import streamlit as st

st.set_page_config(page_title="Cricbuzz LiveStats", layout="wide")

st.title("🏏 Cricbuzz LiveStats")
st.write("Live cricket scores and analytics powered by RapidAPI + Streamlit.")

# Sidebar Navigation
st.sidebar.title("Navigation")

# 👇 Define menu items in your preferred order
menu_items = [
    "Home",
    "Live Matches",
    "Top Stats",
    "SQL Analytics",
    "CRUD"
]

menu = st.sidebar.radio("Select a Page:", menu_items)

# Display page content based on selection
if menu == "Home":
    st.subheader("🏠 Home")
    st.write("Welcome to Cricbuzz LiveStats! Explore live scores, stats, and analytics.")

elif menu == "Live Matches":
    st.subheader("⚡ Live Matches")
    st.write("Check out the latest live cricket matches and real-time updates.")

elif menu == "Top Stats":
    st.subheader("📊 Top Stats")
    st.write("View top players, teams, and match statistics.")

elif menu == "SQL Analytics":
    st.subheader("🛠 SQL Analytics")
    st.write("Run analytics and queries on cricket datasets.")

elif menu == "CRUD":
    st.subheader("✏️ CRUD Operations")
    st.write("Create, Read, Update, and Delete records from your cricket database.")
