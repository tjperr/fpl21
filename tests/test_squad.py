from fpl21.squad import Squad
import pytest

GKS = [1, 2]
DEFS = [284, 340, 252, 237, 16]
MIDS = [174, 230, 233, 277, 359]
ATTS = [357, 177, 149]

VALID_SQUAD = GKS + DEFS + MIDS + ATTS
INVALID_SQUAD = VALID_SQUAD[:14] + [20]  # 4 Arsenal players
VALID_SELECTION = GKS[:1] + DEFS[:4] + MIDS[:4] + ATTS[:2]


def test_squad_creation():
    with pytest.raises(ValueError) as e:
        Squad([1, 2, 3, 4, 5])  # not enough players
    assert "required, you have" in str(e.value)

    with pytest.raises(ValueError) as e:
        Squad(INVALID_SQUAD)  # too many Arsenal players
    assert "At most three players from one PL team allowed" in str(e.value)

    Squad(VALID_SQUAD)


def test_squad_selection():

    s = Squad(VALID_SQUAD)

    with pytest.raises(ValueError) as e:
        s.select_team([1, 2, 3])
    assert "must have 11 players" in str(e.value)

    with pytest.raises(ValueError) as e:
        s.select_team([100 + i for i in range(11)])
    assert "not in squad" in str(e.value)

    with pytest.raises(ValueError) as e:
        s.select_team(VALID_SQUAD[:11])
    assert "must select one goalkeeper" in str(e.value)

    s.select_team(VALID_SELECTION)


def test_position_attributes():
    s = Squad(VALID_SQUAD)

    assert s.goalkeepers == GKS
    assert s.defenders == DEFS
    assert s.midfielders == MIDS
    assert s.attackers == ATTS

def test_transfer_checks_position():
    with pytest.raises(ValueError) as e:
        Squad(VALID_SQUAD).transfer(1, 100)
    assert "Position of transfer player doesn't match" in str(e.value)

def test_transfer_checks_in_player():
    with pytest.raises(ValueError) as e:
        Squad(VALID_SQUAD).transfer(1, 2)    
    assert "already in squad" in str(e.value)
    
def test_transfer_checks_out_player():
    with pytest.raises(ValueError) as e:
        Squad(VALID_SQUAD).transfer(3, 4)    
    assert "not in squad" in str(e.value)