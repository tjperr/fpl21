import asyncio

import aiohttp
from fpl import FPL
from fpl21.utils import pp


def execute(func):
    def new_func(*args, **kwargs):
        return asyncio.run(func(*args, *kwargs))

    return new_func


@execute
async def get_players(pids):
    async with aiohttp.ClientSession() as session:
        fpl = FPL(session)
        players = await fpl.get_players(pids, return_json=True)
    return players


def get_player(pid):
    return list(get_players([pid])).pop()


@execute
async def get_team(tid):
    async with aiohttp.ClientSession() as session:
        fpl = FPL(session)
        team = await fpl.get_team(tid, return_json=True)
    return team


@execute
async def get_player_summaries(pids=None):

    async with aiohttp.ClientSession() as session:
        fpl = FPL(session)
        players = await fpl.get_player_summaries(player_ids=pids, return_json=True)
    return players


@execute
async def get_fixtures():
    async with aiohttp.ClientSession() as session:
        fpl = FPL(session)
        fixtures = await fpl.get_fixtures(return_json=True)
    return fixtures


# a = get_players([2])
# b=get_player_summaries([2])

# pp(a)
# print('-'* 100)
# pp(list(b)[0])
# print([x for x in a if x not in b])
# print([x for x in b if x not in a])


# Whats the difference between player and player summary?
# what the core here for model building and prediction
