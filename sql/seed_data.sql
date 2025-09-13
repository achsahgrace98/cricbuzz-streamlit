-- Insert Teams
INSERT INTO teams (id, name, country, code) VALUES
(1, 'India', 'India', 'IND'),
(2, 'Australia', 'Australia', 'AUS'),
(3, 'England', 'England', 'ENG');

-- Insert Players
INSERT INTO players (id, name, country, playing_role, batting_style, bowling_style, dob, is_captain) VALUES
(1, 'Virat Kohli', 'India', 'Batsman', 'Right-hand bat', 'Right-arm medium', '1988-11-05', 0),
(2, 'Rohit Sharma', 'India', 'Batsman', 'Right-hand bat', 'Off break', '1987-04-30', 1),
(3, 'Hardik Pandya', 'India', 'Allrounder', 'Right-hand bat', 'Right-arm fast-medium', '1993-10-11', 0),
(4, 'Jasprit Bumrah', 'India', 'Bowler', 'Right-hand bat', 'Right-arm fast', '1993-12-06', 0),
(5, 'MS Dhoni', 'India', 'Wicketkeeper', 'Right-hand bat', 'Right-arm medium', '1981-07-07', 1),
(6, 'Steve Smith', 'Australia', 'Batsman', 'Right-hand bat', 'Right-arm legbreak', '1989-06-02', 1),
(7, 'David Warner', 'Australia', 'Batsman', 'Left-hand bat', 'Right-arm legbreak', '1986-10-27', 0),
(8, 'Pat Cummins', 'Australia', 'Bowler', 'Right-hand bat', 'Right-arm fast', '1993-05-08', 1),
(9, 'Joe Root', 'England', 'Batsman', 'Right-hand bat', 'Right-arm offbreak', '1990-12-30', 1),
(10, 'Ben Stokes', 'England', 'Allrounder', 'Left-hand bat', 'Right-arm fast-medium', '1991-06-04', 0);

-- Insert Venues
INSERT INTO venues (id, name, city, country, capacity) VALUES
(1, 'Wankhede Stadium', 'Mumbai', 'India', 33000),
(2, 'MCG', 'Melbourne', 'Australia', 100000);

-- Insert Matches
INSERT INTO matches (id, series, team1_id, team2_id, venue_id, start_date, winner_id, toss_winner_id, toss_decision, status) VALUES
(1001, 'Border-Gavaskar Trophy', 1, 2, 1, '2023-02-09', 1, 2, 'bat', 'Completed'),
(1002, 'Ashes', 2, 3, 2, '2023-06-15', 3, 3, 'field', 'Completed'),
(1003, 'India vs England T20', 1, 3, 1, '2023-12-01', 1, 1, 'bat', 'Completed');

-- Insert Player Stats
INSERT INTO player_stats (player_id, match_id, format, runs, balls, fours, sixes, wickets, overs, economy, catches, stumpings) VALUES
(1, 1001, 'Test', 120, 200, 12, 2, 0, 0, 0, 1, 0),
(2, 1001, 'Test', 45, 80, 6, 0, 0, 0, 0, 0, 0),
(3, 1001, 'Test', 30, 40, 3, 1, 2, 12, 3.5, 0, 0),
(4, 1001, 'Test', 10, 15, 1, 0, 4, 20, 2.8, 0, 0),
(6, 1001, 'Test', 95, 150, 10, 1, 0, 0, 0, 2, 0),

(7, 1002, 'Test', 180, 220, 20, 2, 0, 0, 0, 1, 0),
(8, 1002, 'Test', 15, 25, 2, 0, 5, 25, 3.2, 0, 0),
(9, 1002, 'Test', 150, 210, 14, 1, 0, 0, 0, 1, 0),
(10, 1002, 'Test', 80, 120, 8, 2, 3, 15, 3.0, 1, 0),

(1, 1003, 'T20', 75, 50, 8, 3, 0, 0, 0, 0, 0),
(2, 1003, 'T20', 60, 40, 7, 2, 0, 0, 0, 1, 0),
(9, 1003, 'T20', 55, 35, 6, 3, 0, 0, 0, 0, 0),
(10, 1003, 'T20', 20, 15, 2, 1, 2, 4, 5.0, 0, 0);

-- Insert Partnerships
INSERT INTO partnerships (match_id, player1_id, player2_id, runs) VALUES
(1001, 1, 2, 150),
(1001, 3, 4, 45),
(1002, 7, 9, 200),
(1003, 1, 2, 100),
(1003, 9, 10, 60);
