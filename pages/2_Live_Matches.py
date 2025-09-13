import streamlit as st
import requests

st.set_page_config(page_title="Live Matches", page_icon="🏏")

st.title("🏏 Live Matches")

# ✅ Cache API response for 1 minute to avoid hitting rate limits
@st.cache_data(ttl=60)
def get_live_matches():
    url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/live"
    headers = {
        "X-RapidAPI-Key": st.secrets["RAPIDAPI_KEY"],  # safer than hardcoding
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

try:
    data = get_live_matches()

    # 🔹 Display matches if available
    if "typeMatches" in data:
        for match_type in data["typeMatches"]:
            st.subheader(match_type.get("matchType", "Unknown"))

            if "seriesMatches" in match_type:
                for series in match_type["seriesMatches"]:
                    series_name = series.get("seriesAdWrapper", {}).get("seriesName", "Unknown Series")
                    st.markdown(f"**{series_name}**")

                    matches = series.get("seriesAdWrapper", {}).get("matches", [])
                    for m in matches:
                        match_info = m.get("matchInfo", {})
                        teams = match_info.get("team1", {}).get("teamSName", "") + " vs " + \
                                match_info.get("team2", {}).get("teamSName", "")
                        status = match_info.get("status", "No status available")
                        st.write(f"- {teams} — {status}")
    else:
        st.info("No live matches available right now.")

except Exception as e:
    st.error(f"Could not load matches: {e}")
