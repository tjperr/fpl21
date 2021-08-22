from typing import List
import pytest
from fpl21.connection import (
    _get_players,
    _get_fixtures,
    _get_team,
)


def test_get_players():
    obj = _get_players([1, 2])
    assert [p["id"] for p in obj] == [1, 2]

    # check player summaries included
    assert 'history' in obj[0].keys()


def test_get_all_players():
    obj = _get_players()
    assert len(obj) > 11 * 20  # 11 players, 20 teams


def test_get_fixtures():
    obj = _get_fixtures()
    assert len(obj) == 20 * 19


def test_get_team():
    obj = _get_team(2)
    assert obj["name"] == "Aston Villa"
