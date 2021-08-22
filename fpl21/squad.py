import collections

from fpl21.data import get_position, get_team, get_value, name_list


def check_valid_number(pids, pos_name, valid_range, valid_range_name):
    if len(pids) not in valid_range:
        raise ValueError(
            f"must select {valid_range_name} {pos_name}, {len(pids)} given:{name_list(pids)}"
        )


def check_n_from_pl_team(pids):
    """
    Check not too many playesfrom the same pl team
    """
    teams = collections.Counter([get_team(pid) for pid in pids])
    for k, v in teams.items():
        if v > 3:
            raise ValueError(
                f"""
                At most three players from one PL team allowed.
                You have {v} players from team {k}:
                {name_list([p for p in pids if get_team(p) == k])})
            """
            )

    return


class Squad:
    def __init__(self, pids):
        self.players = pids
        self.validate()

    def validate(self):
        check_n_from_pl_team(self.players)
        check_valid_number(self.goalkeepers, "goalkeeper", [2], "two"),
        check_valid_number(self.defenders, "defenders", [5], "five")
        check_valid_number(
            self.midfielders,
            "midfielders",
            [5],
            "five",
        )
        check_valid_number(self.attackers, "attackers", [3], "three")

    @property
    def goalkeepers(self):
        return [pid for pid in self.players if get_position(pid) == 1]

    @property
    def defenders(self):
        return [pid for pid in self.players if get_position(pid) == 2]

    @property
    def midfielders(self):
        return [pid for pid in self.players if get_position(pid) == 3]

    @property
    def attackers(self):
        return [pid for pid in self.players if get_position(pid) == 4]

    def value(self):
        return sum(get_value(pid) for pid in self.players)

    def select_team(self, pids):
        """select a starting 11"""
        if len(pids) != 11:
            raise ValueError(f"Starting 11 must have 11 players, {len(pids)} given")

        for p in pids:
            if p not in self.players:
                raise ValueError(f"player {name_list([p])} not in squad!")

        check_valid_number(
            [p for p in pids if get_position(p) == 1], "goalkeeper", [1], "one"
        )
        check_valid_number(
            [p for p in pids if get_position(p) == 2], "defenders", [3, 4, 5], "3-5"
        )
        check_valid_number(
            [p for p in pids if get_position(p) == 3],
            "mids",
            [3, 4, 5],
            "3-5",
        )
        check_valid_number(
            [p for p in pids if get_position(p) == 4], "attackers", [1, 2, 3], "1-3"
        )

        self.selection = pids

    def __repr__(self):

        return f"""
    Team of {len(self.players)} players:
    Goalkeepers:
        {name_list(self.goalkeepers)}
    Defenders:
        {name_list(self.defenders)}
    Midfielders:
        {name_list(self.midfielders)}
    Attckers:
        {name_list(self.attackers)}
    """

    def transfer(self, out_pid, in_pid):

        if out_pid not in self.players:
            raise ValueError(f"out player {name_list([out_pid])} not in squad!")

        if in_pid in self.players:
            raise ValueError(f"in player {name_list([in_pid])} already in squad!")

        # This also ensures number of players in each position is still fine
        if get_position(in_pid) != get_position(out_pid):
            raise ValueError(
                f"""Position of transfer player doesn't match:
                In: {name_list([in_pid])} (position {(get_position(in_pid))})
                Out: {name_list([out_pid])} (position {(get_position(out_pid))})
                """
            )

        #
        # TODO check have enough money!
        #

        # [:] because don't want to modify self.players in place
        new_pids = self.players[:]
        new_pids.remove(out_pid)
        new_pids.append(in_pid)

        check_n_from_pl_team(new_pids)
        self.players = new_pids
