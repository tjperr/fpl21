from fpl21.squad import Squad
import pytest

GKS = [1, 2]
DEFS = [9, 10, 11, 14, 16]
MIDS = [3, 7, 12, 13, 17]
ATTS = [4, 6, 20]
VALID_SQUAD = GKS + DEFS + MIDS + ATTS
VALID_SELECTION = GKS[:1] + DEFS[:4] + MIDS[:4] + ATTS[:2]


def test_squad_creation():
    with pytest.raises(ValueError):
        s = Squad([1, 2, 3, 4, 5])

    s = Squad(VALID_SQUAD)
    print(s)


def test_squad_selection():
    s = Squad(VALID_SQUAD)

    with pytest.raises(ValueError):
        s.select_team([1, 2, 3])

    with pytest.raises(ValueError):
        s.select_team([100 + i for i in range(11)])

    with pytest.raises(ValueError):
        s.select_team(VALID_SQUAD[:11])

    s.select_team(VALID_SELECTION)
