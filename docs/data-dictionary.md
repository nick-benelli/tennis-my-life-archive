# Tennis is My Life Data Dictionary

From: [Tennis Is My Life - Match Database](https://stats.tennismylife.org/tennis-match-database)

## Documentation

TennisMyLife hosts a comprehensive tennis match database, including all historical match data, ATP and WTA player stats, and ongoing tournament results. All datasets are available as CSV downloads, making it easy for analysts, fans, and developers to explore tennis statistics.

There are many other tennis databases out there, but TennisMyLife stands out. Unlike Sackmann's database, we use ATP player IDs, providing a more convenient way to calculate player records and cross-reference data directly on the official ATP website.

## Database Columns

### Tournament

| Column | Description |
| --- | --- |
| `tourney_id` | Tournament ID based on ATP database |
| `tourney_name` | City where the tournament was played |
| `surface` | Hard, clay, grass, carpet |
| `draw_size` | Tournament draw (128, 64, 32, 16, 8, 4) |
| `tourney_level` | `G` (Grand Slam), `A` (ATP Tour), `D` (Davis Cup), `F` (Masters/ATP Finals) |
| `indoor` | Yes/No |
| `tourney_date` | Week of the tournament (YYYYMMDD) |
| `match_num` | Match number in the tournament |

### Winner

| Column | Description |
| --- | --- |
| `winner_id` | ATP player ID of the winner |
| `winner_seed` | Seed of the winner |
| `winner_entry` | How the winner entered the tournament (e.g., Q, WC) |
| `winner_name` | Full name of the winner |
| `winner_hand` | Playing hand of the winner (R/L) |
| `winner_ht` | Height of the winner in cm |
| `winner_ioc` | Country code of the winner |
| `winner_age` | Age of the winner at match time |
| `winner_rank` | ATP ranking of the winner at match time |
| `winner_rank_points` | ATP ranking points of the winner at match time |

### Loser

| Column | Description |
| --- | --- |
| `loser_id` | ATP player ID of the loser |
| `loser_seed` | Seed of the loser |
| `loser_entry` | How the loser entered the tournament |
| `loser_name` | Full name of the loser |
| `loser_hand` | Playing hand of the loser (R/L) |
| `loser_ht` | Height of the loser in cm |
| `loser_ioc` | Country code of the loser |
| `loser_age` | Age of the loser at match time |
| `loser_rank` | ATP ranking of the loser at match time |
| `loser_rank_points` | ATP ranking points of the loser at match time |

### Match

| Column | Description |
| --- | --- |
| `score` | Final match score (set by set) |
| `best_of` | Number of sets (3 or 5) |
| `round` | R128, R64, R32, R16, QF, SF, F |
| `minutes` | Match duration in minutes |

### Winner Stats

| Column | Description |
| --- | --- |
| `w_ace` | Aces by winner |
| `w_df` | Double faults by winner |
| `w_svpt` | Total serve points by winner |
| `w_1stIn` | First serves in by winner |
| `w_1stWon` | First serve points won by winner |
| `w_2ndWon` | Second serve points won by winner |
| `w_SvGms` | Service games played by winner |
| `w_bpSaved` | Break points saved by winner |
| `w_bpFaced` | Break points faced by winner |

### Loser Stats

| Column | Description |
| --- | --- |
| `l_ace` | Aces by loser |
| `l_df` | Double faults by loser |
| `l_svpt` | Total serve points by loser |
| `l_1stIn` | First serves in by loser |
| `l_1stWon` | First serve points won by loser |
| `l_2ndWon` | Second serve points won by loser |
| `l_SvGms` | Service games played by loser |
| `l_bpSaved` | Break points saved by loser |
| `l_bpFaced` | Break points faced by loser |

## Updates

We continuously monitor ATP and WTA updates, including additions, corrections, and removals from historical records. Our database is also enriched with verified data from newspapers, tennis blogs, and other statistics websites.

### Frequent Updates & Live Results

TennisMyLife is updated daily, and ideally in real-time, following live ATP match results. We aim to provide fresh tennis statistics without waiting for weekly summaries.

We welcome collaborations and bug reports. Help us improve the quality of this tennis database and make it the most reliable source for ATP and WTA stats, match history, and player analytics.