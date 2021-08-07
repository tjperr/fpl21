from fpl21.connection import get_player, get_players
from fpl21.utils import pp

players_list = get_players(None)
players_dict = {x['id']: x for x in players_list}

pp(players_dict)
for k, v in players_dict.items():
    v['name'] = v["first_name"] + " " + v["second_name"]

def get_position(pid):
    return players_dict[pid]['element_type']