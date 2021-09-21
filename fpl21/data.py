import json
import random

import matplotlib as pyplot
import numpy as np
import pandas as pd
from tqdm import tqdm

from fpl21.connection import _get_players
from fpl21.utils import pp

# Load the players_list from file or call the API
try:
    with open("players_list.json", "r") as f:
        print("loading players list from file")
        players_list = json.load(f)
except FileNotFoundError:
    print("players list not found, calling API")
    players_list = _get_players()

    print("Saving to file players_list.json ...")

    with open("players_list.json", "w") as out_file:
        json.dump(players_list, out_file)

players_info_dict = {x["id"]: x for x in players_list}

for k, v in players_info_dict.items():
    v["name"] = v["first_name"] + " " + v["second_name"]

######################################################################
# Basic fetch methods
######################################################################


def get_player_ids():
    return list(players_info_dict.keys())


def get_player(pid):
    return players_info_dict[pid]


def name_list(pids):
    return "\n\t".join([str(pid) + ": " + get_name(pid) for pid in pids])


def get_position(pid):
    return players_info_dict[pid]["element_type"]


def get_name(pid):
    player = players_info_dict[pid]
    return f"""{player["first_name"]} {player["second_name"]}"""


def get_value(pid):
    # return players_info_dict[pid]["now_cost"] # buying price
    # latest value
    return players_info_dict[pid]["history"][-1]["value"]


def get_team(pid):
    return players_info_dict[pid]["team_code"]


######################################################################
# Dataframe creation methods
######################################################################


def create_player_attrs_df():
    """Create a player attrs dataframe"""

    keys = [
        "id",
        "web_name",
        "element_type",
        "team",
        "ep_this",
        "ep_next",
        "chance_of_playing_this_round",
    ]

    return pd.DataFrame(
        [[p[key] for key in keys] for p in players_info_dict.values()], columns=keys
    ).rename(columns={"id": "element"})


def create_history_df():
    hist = [p["history"] for p in players_info_dict.values()]
    df = pd.DataFrame([x for sublist in hist for x in sublist])
    return df.rename(columns={"was_home": "is_home"})


def create_team_stats_df():

    player_attrs_df = create_player_attrs_df()
    history_df = create_history_df()

    # Work out team metrics per minute played. This handles transfers, varying number of fixtures and having a large
    # squad where lots of players don't get gametime and so have 0 points
    team_data = (
        history_df.merge(player_attrs_df, on="element")
        .groupby("team")
        .agg(
            {
                "total_points": np.sum,
                "goals_scored": np.sum,
                "goals_conceded": np.sum,
                "minutes": np.sum,
            }
        )
    )
    team_data["team_points_per_game"] = (
        90 * 11 * team_data.total_points / team_data.minutes
    )
    team_data["team_goals_conceded_per_game"] = (
        90 * team_data.goals_conceded / team_data.minutes
    )  # already counted for every player
    team_data["team_goals_scored_per_game"] = (
        90 * 11 * team_data.goals_scored / team_data.minutes
    )

    return team_data[
        [
            "team_points_per_game",
            "team_goals_conceded_per_game",
            "team_goals_scored_per_game",
        ]
    ]


def create_fixtures_df():

    entries = []
    for k, v in players_info_dict.items():
        fixtures = v["fixtures"]
        for f in fixtures:
            f["element"] = k
            entries.append(f)

    df = pd.DataFrame(entries)
    return df


create_fixtures_df()
