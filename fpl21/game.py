import random
import numpy as np
from fpl21.squad import Squad
from fpl21.utils import pp


# dummy function for development
# returns a predicted score for a player
def player_score(pid):
    # lets see if MC can find this player!
    if pid == 252:
        return 10
    # and favour even ids
    if pid % 2 == 0:
        return random.choice(range(11))    
    return random.choice(range(10))


my_squad = Squad([30, 80, 275, 198, 110, 252, 62, 22, 35, 196, 277, 359, 413, 337, 189])
score_dict = {pid: [] for pid in my_squad.players}

# MC for team selection
for _ in range(1000):
    team = (
        random.sample(my_squad.goalkeepers, 1)
        + random.sample(my_squad.defenders, 3)
        + random.sample(my_squad.midfielders, 4)
        + random.sample(my_squad.attackers, 3)
    )

    my_squad.select_team(team)
    score = sum(player_score(pid) for pid in my_squad.selection)

    for pid in my_squad.selection:
        score_dict[pid].append(score)
    
summary_score_dict = {}
for pid, scores in score_dict.items():
    summary_score_dict[pid] = np.mean(scores)

import pandas as pd
scores_df = pd.DataFrame({
    "pid": score_dict.keys(),
    "avg_score": [np.mean(scores) for scores in score_dict.values()]
})

# print the best 11 playes, no checking whether this is a valid team atm
print(scores_df.sort_values(by="avg_score", ascending=False)[:11])