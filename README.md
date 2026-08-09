# Boot Room

A ten-round football drafting game with a career simulator. 360 players across 18 squad-seasons, 20 per squad. Every spin deals a real squad from the last twenty years
— Manchester United 2007-08, Barcelona 2010-11, Chelsea 2009-10 — and you draft one player
from it for one attribute. One weak link drags the whole build down.

**Play:** https://jujubug007.github.io/boot-room/

### The ten categories
Finishing · Passing · Defending · Creativity · Soccer IQ · Dribbling · Physical · Height ·
Weak Foot · Skill Moves

### About the ratings
All ratings are original estimates — nothing scraped, no third-party data. Seven are
judgement calls on a position-normalised scale, so a centre-back's Finishing of 24 and a
striker's Defending of 24 both mean "poor for that role". Three are derived from real facts:
Height from actual centimetres, Weak Foot and Skill Moves from the familiar five-star scales.

`make_own_pool.py` regenerates `players.json`. Edit the squad tables to add your own.

### Career mode
Finish a draft and the build is simulated across a full career - club moves up and down a
ladder as the rating rises and falls with age, appearances, goals, honours, injuries and a
closing verdict. Re-roll the luck without rebuilding the player.

### Respins
Four, one use each: **squad** (new club-season), **year** (same club, different season),
**board** (same squad, different five), **attribute** (same board, different category).

### Scoring
Blend of your average and your worst pick, weighted toward the worst. Tier thresholds were
calibrated by simulation: 30 drafts of perfect play span 69-87, random play medians 59.
