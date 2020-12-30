player_data = {
              "username": 'USER00',
              "rating": 1400,
              "wins": 0,
              "losses": 0,
              "draws": 0,
              "bnae": 1,
              "avnoz": 'DEFAULT',
              "main_guild": 'DEFAULT'
              }


class Player:
    """CREATE THE PLAYER HERE"""
    def __init__(self, player_data):
        self.player_data = player_data
        self.player_data["username"] = player_data["username"]
        self.player_data["rating"] = player_data["rating"]
        self.player_data["wins"] = player_data["wins"]
        self.player_data["losses"] = player_data["losses"]
        self.player_data["draws"] = player_data["draws"]
        self.player_data["bnae"] = player_data["bnae"]
        self.player_data["avnoz"] = player_data["avnoz"]
        self.player_data["main_guild"] = player_data["main_guild"]
