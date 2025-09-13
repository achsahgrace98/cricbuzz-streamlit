from utils.api_client import get_live_matches
from utils.db_connection import get_connection

def sync_matches_to_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS matches (id INTEGER PRIMARY KEY, series TEXT, team1 TEXT, team2 TEXT, status TEXT)")

    data = get_live_matches()
    for tm in data.get("typeMatches", []):
        for series in tm.get("seriesMatches", []):
            matches = series.get("seriesAdWrapper", {}).get("matches", [])
            for m in matches:
                info = m.get("matchInfo", {})
                mid = info.get("matchId")
                series_name = info.get("seriesName")
                team1 = info.get("team1", {}).get("teamName")
                team2 = info.get("team2", {}).get("teamName")
                status = info.get("status")

                cur.execute("INSERT OR REPLACE INTO matches (id, series, team1, team2, status) VALUES (?,?,?,?,?)",
                            (mid, series_name, team1, team2, status))
    conn.commit()
    conn.close()
