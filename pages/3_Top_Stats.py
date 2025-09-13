import streamlit as st
import pandas as pd
from utils.db_connection import get_connection

st.title("🌟 Top Player Stats")

query = """
SELECT p.name, SUM(ps.runs) as total_runs, SUM(ps.wickets) as total_wickets
FROM player_stats ps
JOIN players p ON ps.player_id = p.id
GROUP BY p.name
ORDER BY total_runs DESC
LIMIT 10;
"""

conn = get_connection()
df = pd.read_sql_query(query, conn)
st.subheader("🏏 Top 10 Run Scorers")
st.dataframe(df)
conn.close()
