from typing import List

import pytest

from fpl21.connection import _get_fixtures, _get_players, _get_team

# Don't run these tests by default:
reason = "Limit # requests to fpl API"
DO_NOT_RUN = True


@pytest.mark.skipif(DO_NOT_RUN, reason=reason)
def test_get_players():
    obj = _get_players([1, 2])
    assert [p["id"] for p in obj] == [1, 2]

    # check player summaries included
    assert "history" in obj[0].keys()


@pytest.mark.skipif(DO_NOT_RUN, reason=reason)
def test_get_all_players():
    obj = _get_players()
    assert len(obj) > 11 * 20  # 11 players, 20 teams


@pytest.mark.skipif(DO_NOT_RUN, reason=reason)
def test_get_fixtures():
    obj = _get_fixtures()
    assert len(obj) == 20 * 19


@pytest.mark.skipif(DO_NOT_RUN, reason=reason)
def test_get_team():
    obj = _get_team(2)
    assert obj["name"] == "Aston Villa"
