from typing import List
import pytest
from fpl21.connection import (
    get_player,
    get_players,
    get_player_summaries,
    get_fixtures,
    get_team,
)


def test_get_players():
    obj = get_players([1, 2])
    assert [o["id"] for o in obj] == [1, 2]


def test_get_all_players():
    obj = get_players(None)
    assert len(obj) > 11 * 20


def test_get_player_summaries():
    obj = get_player_summaries([1])
    assert "fixtures" in list(obj)[0].keys()


def test_get_fixtures():
    obj = get_fixtures()
    assert len(obj) == 20 * 19


def test_get_team():
    obj = get_team(2)
    assert obj["name"] == "Aston Villa"
