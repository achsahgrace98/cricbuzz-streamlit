import streamlit as st
import sqlite3
from utils.db_connection import get_connection

st.header("🛠️ CRUD Operations on Players")

conn = get_connection()
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS players (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, country TEXT)")
conn.commit()

menu = ["Create", "Read", "Update", "Delete"]
choice = st.selectbox("Action", menu)

if choice == "Create":
    name = st.text_input("Player Name")
    country = st.text_input("Country")
    if st.button("Add Player"):
        cur.execute("INSERT INTO players (name, country) VALUES (?,?)", (name, country))
        conn.commit()
        st.success("Player added!")

elif choice == "Read":
    cur.execute("SELECT * FROM players")
    rows = cur.fetchall()
    st.table(rows)

elif choice == "Update":
    cur.execute("SELECT * FROM players")
    data = cur.fetchall()
    player = st.selectbox("Select player to update", data, format_func=lambda x: f"{x[1]} ({x[2]})")
    new_name = st.text_input("New Name", player[1])
    new_country = st.text_input("New Country", player[2])
    if st.button("Update"):
        cur.execute("UPDATE players SET name=?, country=? WHERE id=?", (new_name, new_country, player[0]))
        conn.commit()
        st.success("Player updated!")

elif choice == "Delete":
    cur.execute("SELECT * FROM players")
    data = cur.fetchall()
    player = st.selectbox("Select player to delete", data, format_func=lambda x: f"{x[1]} ({x[2]})")
    if st.button("Delete"):
        cur.execute("DELETE FROM players WHERE id=?", (player[0],))
        conn.commit()
        st.warning("Player deleted!")

conn.close()
