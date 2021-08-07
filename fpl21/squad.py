from fpl21.data import get_position, get_name, name_list


class Squad:
    def __init__(self, team):
        self.goalkeepers = [pid for pid in team if get_position(pid) == 1]
        self.defenders = [pid for pid in team if get_position(pid) == 2]
        self.midfielders = [pid for pid in team if get_position(pid) == 3]
        self.attackers = [pid for pid in team if get_position(pid) == 4]
        self.players = team
        self.validate()

    def validate(self):
        if len(self.goalkeepers) != 2:
            raise ValueError(
                f"2 goalkeepers required, you have {len(self.goalkeepers)}"
            )
        if len(self.defenders) != 5:
            raise ValueError(f"5 defenders required, you have {len(self.defenders)}")
        if len(self.midfielders) != 5:
            raise ValueError(
                f"5 midfielders required, you have {len(self.midfielders)}"
            )
        if len(self.attackers) != 3:
            raise ValueError(
                f"""3 attackers required, you have {len(self.attackers)}"""
            )
        return

    def select_team(self, pids):
        """select a starting 11"""
        if len(pids) != 11:
            raise ValueError(f"Starting 11 must have 11 players, {len(pids)} given")

        for p in pids:
            if p not in self.players:
                raise ValueError(f"player {name_list([p])} not in squad!")

        gks = [p for p in pids if p in self.goalkeepers]
        defs = [p for p in pids if p in self.defenders]
        mids = [p for p in pids if p in self.midfielders]
        atts = [p for p in pids if p in self.attackers]

        if len(gks) != 1:
            raise ValueError(
                f"must select one goalkeeper, {len(gks)} given: {name_list(gks)}"
            )
        if len(defs) not in [3, 4, 5]:
            raise ValueError(
                f"must select 3 - 5 defenders, {len(defs)} given: {name_list(defs)}"
            )

        if len(mids) not in [3, 4, 5]:
            raise ValueError(
                f"must select 3 - 5 midfielders, {len(mids)} given: {name_list(mids)}"
            )

        if len(atts) not in [1, 2, 3]:
            raise ValueError(
                f"must select 1 - 3 attackers, {len(atts)} given: {name_list(atts)}"
            )

        # TODO: Need to validate not more than three players from the same team

    def __repr__(self):

        gks = ", ".join(name_list(self.goalkeepers))
        defs = ", ".join(name_list(self.defenders))
        mid = ", ".join(name_list(self.midfielders))
        att = ", ".join(name_list(self.attackers))
        return f""" Team of {len(self.players)} players:
        Goalkeepers: {gks}
        Defenders: {defs}
        Midfielders: {mid}
        Attckers: {att}
        """

    # def transfer(in_id, out_id):
    #     if position(in_id) != position(out_id):
    #         raise ValueError("Position of transfer player doesn't match")
    #     else:
    #         self.team[]
