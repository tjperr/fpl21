import random
import numpy as np
import pandas as pd
from tqdm import tqdm

from collections import defaultdict
from fpl21.squad import Squad
from fpl21.data import get_player, get_player_ids, get_position, get_name


def player_score(pid):
    return float(get_player(pid)["ep_next"])


score_dict = defaultdict(list)

# MC for team selection
for _ in tqdm(range(100_000), desc="Simulating"):

    my_squad = Squad(
        [30, 80, 275, 198, 110, 252, 62, 22, 35, 196, 277, 359, 413, 337, 189]
    )

    # Probably want to weight transfers too - sample space is otherwise too large
    transfer_in = random.choice(get_player_ids())
    transfer_out = random.choice(
        my_squad.get_players_with_position(get_position(transfer_in))
    )

    try:
        my_squad.transfer(transfer_out, transfer_in)
        param = get_name(transfer_out) + " -> " + get_name(transfer_in)

    except ValueError:
        param = "NO_TRANSFER"
        pass

    # TODO: Weight team selection based on expected points, to avoid suggesting a squad where every
    # selected team does well (Points on the bench dont matter!)
    formation = random.choice(
        [[3, 4, 3], [3, 5, 2], [4, 3, 3], [4, 4, 2], [4, 5, 1], [5, 3, 2], [5, 4, 1]]
    )
    team = (
        random.sample(my_squad.goalkeepers, 1)
        + random.sample(my_squad.defenders, formation[0])
        + random.sample(my_squad.midfielders, formation[1])
        + random.sample(my_squad.attackers, formation[2])
    )

    my_squad.select_team(team)
    score = sum(player_score(pid) for pid in my_squad.selection)

    score_dict[param].append(score)


scores_df = pd.DataFrame(
    {
        "param": score_dict.keys(),
        "avg_score": [np.mean(scores) for scores in score_dict.values()],
        "count": [len(scores) for scores in score_dict.values()],
    }
)

# print the best 11 playes, no checking whether this is a valid team atm
print(scores_df.sort_values(by="avg_score", ascending=False)[:11])
