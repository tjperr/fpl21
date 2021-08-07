
class Squad:
    

    def __init__(self, team):
        self.goalkeepers = [pid for pid in team if players[f"{pid}"]["position"] == 1]
        self.defenders = [pid for pid in team if players[f"{pid}"]["position"] == 2]
        self.midfielders = [pid for pid in team if players[f"{pid}"]["position"] == 3]
        self.attackers = [pid for pid in team if players[f"{pid}"]["position"] == 4]
        self.players = team

    def __print__(self):
        return f""" Team of {len(self.team)} players:
        
        """

    # def transfer(in_id, out_id):
    #     if position(in_id) != position(out_id):
    #         raise ValueError("Position of transfer player doesn't match")
    #     else:
    #         self.team[]
