from fpl21.squad import Squad
import pytest

GKS = [1, 2]
DEFS = [284, 340, 252, 237, 16]
MIDS = [174, 230, 233, 277, 359]
ATTS = [357, 177, 149]

VALID_SQUAD = GKS + DEFS + MIDS + ATTS
INVALID_SQUAD = VALID_SQUAD[:14] + [20] # 4 Arsenal players
VALID_SELECTION = GKS[:1] + DEFS[:4] + MIDS[:4] + ATTS[:2]


def test_squad_creation():
    with pytest.raises(ValueError):
        s = Squad([1, 2, 3, 4, 5]) # not enough players

    with pytest.raises(ValueError):
        Squad(INVALID_SQUAD) # too many Arsenal players
    
    s = Squad(VALID_SQUAD)


def test_squad_selection():
    
    s = Squad(VALID_SQUAD)

    with pytest.raises(ValueError):
        s.select_team([1, 2, 3])

    with pytest.raises(ValueError):
        s.select_team([100 + i for i in range(11)])

    with pytest.raises(ValueError):
        s.select_team(VALID_SQUAD[:11])

    
    s.select_team(VALID_SELECTION)

