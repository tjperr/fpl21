import pytest
from fpl21.game import player_score

def test_player_score():
    
    L = [player_score() for _ in range(100)]
    assert max(L) <= 10
    assert min(L) >= 0