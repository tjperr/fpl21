from typing import List
import pytest
from fpl21.manager import get_player, get_player_summaries, get_fixtures, get_team


def test_get_player():
    obj = get_player(1)
    assert obj["id"] == 1


def test_get_player_summaries():
    obj = get_player_summaries()
    assert list(obj)[0]["id"] == 1


def test_get_fixtures():
    obj = get_fixtures()
    assert len(obj) == 20 * 19


def test_get_team():
    obj = get_team(2)
    assert obj["name"] == "Aston Villa"
