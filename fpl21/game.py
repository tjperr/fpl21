import random

from fpl21.squad import Squad
from fpl21.utils import pp


# dummy function for development
# returns a predicted score for a player
def player_score():
    return random.choice(range(10))


my_squad = Squad([30, 80, 275, 198, 110, 252, 62, 22, 35, 196, 277, 359, 413, 337, 189])
print(my_squad)
print(my_squad.value())
