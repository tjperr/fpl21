from fpl21.data import get_name, get_position, get_value, get_team, name_list
import collections


class Squad:
    def __init__(self, pids):
        self.players = pids
        self.validate()

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

    def validate(self):
        if len(self.goalkeepers) != 2:
            raise ValueError(
                f"2 goalkeepers required, you have {len(self.goalkeepers)}: {name_list(self.goalkeepers)}"
            )
        if len(self.defenders) != 5:
            raise ValueError(
                f"5 defenders required, you have {len(self.defenders)}: {name_list(self.defenders)}"
            )
        if len(self.midfielders) != 5:
            raise ValueError(
                f"5 midfielders required, you have {len(self.midfielders)}: {name_list(self.midfielders)}"
            )
        if len(self.attackers) != 3:
            raise ValueError(
                f"""3 attackers required, you have {len(self.attackers)}: {name_list(self.attackers)}"""
            )

        teams = collections.Counter([get_team(pid) for pid in self.players])
        for k, v in teams.items():
            if v > 3:
                raise ValueError(
                    f"""
                    At most three players from one PL team allowed.
                    You have {v} players from team {k}:
                    {name_list([p for p in self.players if get_team(p) == k])})
                """
                )

        return

    def select_team(self, pids):
        """select a starting 11"""
        if len(pids) != 11:
            raise ValueError(f"Starting 11 must have 11 players, {len(pids)} given")

        for p in pids:
            if p not in self.players:
                raise ValueError(f"player {name_list([p])} not in squad!")

        for pos, pos_name, valid_range, valid_range_name in [
            ([p for p in pids if get_position(p) == 1], "goalkeeper", [1], 'one'),
            ([p for p in pids if get_position(p) == 2], "defenders", [3, 4, 5], '3-5'),
            ([p for p in pids if get_position(p) == 3], "midfielders", [3, 4, 5], '3-5'),
            ([p for p in pids if get_position(p) == 4], "attackers", [1, 2, 3], '1-3'),
        ]:
            if len(pos) not in valid_range:
                raise ValueError(
                    f"must select {valid_range_name} {pos_name}, {len(pos)} given:{name_list(pos)}"
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

    # def transfer(in_id, out_id):
    #     if position(in_id) != position(out_id):
    #         raise ValueError("Position of transfer player doesn't match")
    #     else:
    #         self.team[]
