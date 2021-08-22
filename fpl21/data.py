from fpl21.connection import _get_player, _get_players
from fpl21.utils import pp

players_list = _get_players()
players_info_dict = {x["id"]: x for x in players_list}


for k, v in players_info_dict.items():
    v["name"] = v["first_name"] + " " + v["second_name"]


def get_position(pid):
    return players_info_dict[pid]["element_type"]


def get_name(pid):
    return (
        players_info_dict[pid]["first_name"]
        + " "
        + players_info_dict[pid]["second_name"]
    )


def get_value(pid):
    # return players_info_dict[pid]["now_cost"] # buying price
    #latest value
    return players_info_dict[pid]["history"].pop()["value"]


def get_team(pid):
    return players_info_dict[pid]["team_code"]


def name_list(pids):
    return "\n\t".join([str(pid) + ": " + get_name(pid) for pid in pids])
