import streamlit as st
from utils.api_client import get_live_matches

st.title("🏏 Live Matches")

try:
    data = get_live_matches()
    for tm in data.get("typeMatches", []):
        for series in tm.get("seriesMatches", []):
            matches = series.get("seriesAdWrapper", {}).get("matches", [])
            for m in matches:
                info = m.get("matchInfo", {})
                t1 = info.get("team1", {}).get("teamName")
                t2 = info.get("team2", {}).get("teamName")
                status = info.get("status")
                st.write(f"**{t1} vs {t2}** — {status}")
except Exception as e:
    st.error(f"Could not load matches: {e}")
