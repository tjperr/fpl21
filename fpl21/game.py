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
    return random.choice(range(10))


my_squad = Squad([30, 80, 275, 198, 110, 252, 62, 22, 35, 196, 277, 359, 413, 337, 189])
score_dict = {pid: [] for pid in my_squad.players}

# MC for team selection
for _ in range(10000):
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
    
for pid, scores in score_dict.items():
    print(f"{pid:4}: {np.mean(scores):.2f}")

