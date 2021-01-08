team_data = {
              "Epithet": 'default',
              "Rating": 1400,
              "Wins": 0,
              "Losses": 0,
              "Draws": 0,
              "Size": 0,
              "Members": [],
              "Level": 0,
              "Description": "default"
              }


class Team:
    """CREATE THE ALPHRID TEAM HERE"""
    def __init__(self, team_data):
        self.team_data = team_data
        self.team_data["Epithet"] = team_data["Epithet"]
        self.team_data["Rating"] = team_data["Rating"]
        self.team_data["Wins"] = team_data["Wins"]
        self.team_data["Losses"] = team_data["Losses"]
        self.team_data["Draws"] = team_data["Draws"]
        self.team_data["Size"] = team_data["Size"]
        self.team_data["Members"] = team_data["Members"]
        self.team_data["Level"] = team_data["Level"]
        self.team_data["Description"] = team_data["Description"]
