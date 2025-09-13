import streamlit as st
import pandas as pd
from utils.db_connection import get_connection

st.header("📊 SQL Analytics")

# Dictionary of predefined queries
queries = {
    # Beginner
    "1. Players who represent India":
        "SELECT name, country FROM players WHERE country = 'India';",

    "2. Matches in last 30 days":
        "SELECT * FROM matches WHERE DATE(start_date) >= DATE('now', '-30 day');",

    "3. All-rounder players":
        "SELECT * FROM players WHERE playing_role = 'Allrounder';",

    "4. Players who were also captains":
        "SELECT * FROM players WHERE is_captain = 1;",

    "5. Venue details in India":
        "SELECT * FROM venues WHERE country = 'India';",

    "6. Matches played in India":
        "SELECT * FROM matches m JOIN venues v ON m.venue_id = v.id WHERE v.country = 'India';",

    "7. Match summary (desc, teams, venue, start date, status)":
        """SELECT m.id, m.series, m.team1, m.team2, v.name AS venue, m.start_date, m.status
           FROM matches m JOIN venues v ON m.venue_id = v.id;""",

    "8. Matches in 2023":
        "SELECT * FROM matches WHERE strftime('%Y', start_date) = '2023';",

    # Intermediate
    "9. Matches played and won by each team":
        """SELECT team1 AS team, COUNT(*) AS matches_played,
                  SUM(CASE WHEN winner_id = team1_id THEN 1 ELSE 0 END) AS matches_won
           FROM matches GROUP BY team1;""",

    "10. Top 10 highest scorers":
        "SELECT player_id, SUM(runs) AS total_runs FROM player_stats GROUP BY player_id ORDER BY total_runs DESC LIMIT 10;",

    "11. Top 10 bowlers with most wickets":
        "SELECT player_id, SUM(wickets) AS total_wickets FROM player_stats GROUP BY player_id ORDER BY total_wickets DESC LIMIT 10;",

    "12. Player stats with runs > 1000":
        "SELECT player_id, SUM(runs) AS total_runs FROM player_stats GROUP BY player_id HAVING total_runs > 1000;",

    # Advanced
    "13. Player with most runs in T20s":
        "SELECT player_id, SUM(runs) AS total_runs FROM player_stats WHERE format = 'T20' GROUP BY player_id ORDER BY total_runs DESC LIMIT 1;",

    "14. Player with most wickets in Tests":
        "SELECT player_id, SUM(wickets) AS total_wickets FROM player_stats WHERE format = 'Test' GROUP BY player_id ORDER BY total_wickets DESC LIMIT 1;",

    "15. Matches played in each venue":
        "SELECT v.name, COUNT(*) AS matches_played FROM matches m JOIN venues v ON m.venue_id = v.id GROUP BY v.name;",

    "16. Player with most centuries":
        "SELECT player_id, COUNT(*) AS centuries FROM player_stats WHERE runs >= 100 GROUP BY player_id ORDER BY centuries DESC LIMIT 1;",

    "17. Toss advantage analysis":
        """SELECT toss_decision,
                  SUM(CASE WHEN toss_winner_id = winner_id THEN 1 ELSE 0 END) * 100.0 / COUNT(*) AS win_percentage
           FROM matches GROUP BY toss_decision;""",

    "18. Player with most half-centuries":
        "SELECT player_id, COUNT(*) AS fifties FROM player_stats WHERE runs BETWEEN 50 AND 99 GROUP BY player_id ORDER BY fifties DESC LIMIT 1;",

    "19. Best economy rate bowler":
        "SELECT player_id, MIN(economy) AS best_economy FROM player_stats WHERE overs > 10;",

    "20. Player with most ducks":
        "SELECT player_id, COUNT(*) AS ducks FROM player_stats WHERE runs = 0 GROUP BY player_id ORDER BY ducks DESC LIMIT 1;",

    "21. Highest partnership in a match":
        "SELECT match_id, MAX(runs) AS highest_partnership FROM partnerships GROUP BY match_id ORDER BY highest_partnership DESC LIMIT 1;",

    "22. Player with most sixes":
        "SELECT player_id, SUM(sixes) AS total_sixes FROM player_stats GROUP BY player_id ORDER BY total_sixes DESC LIMIT 1;",

    "23. Player with most fours":
        "SELECT player_id, SUM(fours) AS total_fours FROM player_stats GROUP BY player_id ORDER BY total_fours DESC LIMIT 1;",

    "24. Highest strike rate batsman (min 500 balls)":
        """SELECT player_id, (SUM(runs) * 100.0 / SUM(balls)) AS strike_rate
           FROM player_stats GROUP BY player_id HAVING SUM(balls) >= 500
           ORDER BY strike_rate DESC LIMIT 1;""",

    "25. Player with most catches":
        "SELECT player_id, SUM(catches) AS total_catches FROM player_stats GROUP BY player_id ORDER BY total_catches DESC LIMIT 1;"
}

# UI
query_name = st.selectbox("Select a predefined query", list(queries.keys()))
query_sql = queries[query_name]

st.code(query_sql, language="sql")

if st.button("Run Query"):
    try:
        conn = get_connection()
        df = pd.read_sql_query(query_sql, conn)
        st.dataframe(df)
        conn.close()
    except Exception as e:
        st.error(f"Error: {e}")
