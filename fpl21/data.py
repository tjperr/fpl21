from fpl21.connection import get_player, get_players
from fpl21.utils import pp

players_list = get_players(None)
players_dict = {x["id"]: x for x in players_list}

for k, v in players_dict.items():
    v["name"] = v["first_name"] + " " + v["second_name"]


def get_position(pid):
    return players_dict[pid]["element_type"]


def get_name(pid):
    return players_dict[pid]["first_name"] + " " + players_dict[pid]["second_name"]


def get_team(pid):
    return players_dict[pid]["team_code"]


def name_list(pids):
    return [str(pid) + ": " + get_name(pid) for pid in pids]

