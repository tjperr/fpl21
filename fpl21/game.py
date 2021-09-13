import random
from collections import defaultdict

import numpy as np
import pandas as pd
from tqdm import tqdm

from fpl21.data import (
    get_name,
    get_player,
    get_player_ids,
    get_position,
    get_value,
    name_list,
)
from fpl21.squad import Squad

NO_TRANSFER = "NO_TRANSFER"
SQUAD = [30, 80, 275, 262, 110, 245, 62, 272, 35, 144, 277, 359, 413, 337, 189]
CASH = 4

print(Squad(SQUAD, CASH))


def player_score(pid):
    return float(get_player(pid)["ep_next"])


def dist(weights):
    _weights = [max(x, 0.1) for x in weights]
    return [x / sum(_weights) for x in _weights]


score_dict = defaultdict(list)

# MC for transfer/ team selection
for _ in tqdm(range(100_000), desc="Simulating"):

    my_squad = Squad(SQUAD, CASH, validate=False)

    # TODO: Weight transfers by expected points - sample space is otherwise too large
    out_pid = random.choice(my_squad.players)
    available_cash = get_value(out_pid) + my_squad.cash_in_bank
    out_pos = get_position(out_pid)

    options = [
        pid
        for pid in get_player_ids()
        if (get_position(pid) == out_pos) and (get_value(pid) <= available_cash)
    ]
    in_pid = random.choices(options, weights=[player_score(pid) for pid in options])[0]

    try:
        my_squad.transfer(out_pid, in_pid)
        param = get_name(out_pid) + " -> " + get_name(in_pid)

    except ValueError:
        param = NO_TRANSFER
        pass

    # TODO: Weight team selection based on expected points, to avoid suggesting a squad where every
    # selected team does well (Points on the bench dont matter!)
    formation = random.choice(
        [[3, 4, 3], [3, 5, 2], [4, 3, 3], [4, 4, 2], [4, 5, 1], [5, 3, 2], [5, 4, 1]]
    )

    team = (
        list(
            np.random.choice(
                my_squad.goalkeepers,
                1,
                replace=False,
                p=dist([player_score(pid) for pid in my_squad.goalkeepers]),
            )
        )
        + list(
            np.random.choice(
                my_squad.defenders,
                formation[0],
                replace=False,
                p=dist([player_score(pid) for pid in my_squad.defenders]),
            )
        )
        + list(
            np.random.choice(
                my_squad.midfielders,
                formation[1],
                replace=False,
                p=dist([player_score(pid) for pid in my_squad.midfielders]),
            )
        )
        + list(
            np.random.choice(
                my_squad.attackers,
                formation[2],
                replace=False,
                p=dist([player_score(pid) for pid in my_squad.attackers]),
            )
        )
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

# print the best 10 transfers
print(scores_df.sort_values(by="avg_score", ascending=False)[:10])
print(scores_df[scores_df.param == NO_TRANSFER])
