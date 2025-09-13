-- Teams
CREATE TABLE IF NOT EXISTS teams (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    country TEXT,
    code TEXT
);

-- Players
CREATE TABLE IF NOT EXISTS players (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    country TEXT,
    playing_role TEXT,         -- Batsman, Bowler, Allrounder, Wicketkeeper
    batting_style TEXT,        -- Right-hand bat, Left-hand bat
    bowling_style TEXT,        -- Right-arm fast, Left-arm spin
    dob DATE,
    is_captain INTEGER DEFAULT 0  -- 1 if captain
);

-- Venues
CREATE TABLE IF NOT EXISTS venues (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    city TEXT,
    country TEXT,
    capacity INTEGER
);

-- Matches
CREATE TABLE IF NOT EXISTS matches (
    id INTEGER PRIMARY KEY,
    series TEXT,
    team1_id INTEGER,
    team2_id INTEGER,
    venue_id INTEGER,
    start_date DATE,
    winner_id INTEGER,
    toss_winner_id INTEGER,
    toss_decision TEXT,   -- bat or field
    status TEXT,
    FOREIGN KEY(team1_id) REFERENCES teams(id),
    FOREIGN KEY(team2_id) REFERENCES teams(id),
    FOREIGN KEY(venue_id) REFERENCES venues(id),
    FOREIGN KEY(winner_id) REFERENCES teams(id),
    FOREIGN KEY(toss_winner_id) REFERENCES teams(id)
);

-- Player match stats
CREATE TABLE IF NOT EXISTS player_stats (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    player_id INTEGER,
    match_id INTEGER,
    format TEXT,              -- Test, ODI, T20
    runs INTEGER DEFAULT 0,
    balls INTEGER DEFAULT 0,
    fours INTEGER DEFAULT 0,
    sixes INTEGER DEFAULT 0,
    wickets INTEGER DEFAULT 0,
    overs REAL DEFAULT 0,
    economy REAL DEFAULT 0,
    catches INTEGER DEFAULT 0,
    stumpings INTEGER DEFAULT 0,
    FOREIGN KEY(player_id) REFERENCES players(id),
    FOREIGN KEY(match_id) REFERENCES matches(id)
);

-- Partnerships
CREATE TABLE IF NOT EXISTS partnerships (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    match_id INTEGER,
    player1_id INTEGER,
    player2_id INTEGER,
    runs INTEGER,
    FOREIGN KEY(match_id) REFERENCES matches(id),
    FOREIGN KEY(player1_id) REFERENCES players(id),
    FOREIGN KEY(player2_id) REFERENCES players(id)
);
