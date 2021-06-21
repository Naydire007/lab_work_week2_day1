class Team:
    def __init__(self, Name, Players, Coach, points):
        self.Name = Name
        self.Coach = Coach
        self.Players = Players
        self.Players = [
            "Zolt",
            "John",
            "Juan"
        ]
        self.points = points

    def add_player(self,new_player):
      self.Players.append(new_player)

    def has_player(self,players_name):
      players_name == self.Players
      for player in self.Players:
          if player == True: 
            return True 
      else:
         False
    
    def play_game(self, team_won_lost):
      if team_won_lost >= 0:
        self.points += 3
      else:
        self.points == 0