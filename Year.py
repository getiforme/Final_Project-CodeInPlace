
class Year:

    def __init__(self, year_number):
        self.year_number = year_number
        self.players = []  # no students when a section is created! this is a list of Participants

    def add_players(self, player):
        self.players.append(player)

    def get_player_names(self):
        player_names = []

        for player in self.players:
            player_names.append(player.name)
        
        return player_names

