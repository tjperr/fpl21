from fpl import FPL
from utils import pp
import aiohttp
import asyncio


def execute(func, *args, **kwargs):
    def new_func(*args, **kwargs):
        return asyncio.run(func(*args, *kwargs))
    return new_func

@execute
async def get_player(pid):
    async with aiohttp.ClientSession() as session:
        fpl = FPL(session)
        player = await fpl.get_player(pid)
    return player

@execute
async def get_team(tid):
    async with aiohttp.ClientSession() as session:
        fpl = FPL(session)
        team = await fpl.get_team(tid)
    return team


@execute
async def get_player_summaries(pids=None):
    async with aiohttp.ClientSession() as session:
        fpl = FPL(session)
        players = await fpl.get_players(player_ids=pids, return_json=True)
    return players


@execute
async def get_fixtures():
    async with aiohttp.ClientSession() as session:
        fpl = FPL(session)
        fixtures = await fpl.get_fixtures(return_json=True)
    return fixtures


pp(get_player_summaries([2]))
