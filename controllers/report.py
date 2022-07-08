from models.Player import Player, player_database
from models.Tournament import Tournament, tournament_database

class ReportController:
    def __init__(self, view):
        self.view = view

    def get_all_players(self):
        return player_database.all()
    
    def get_all_tournaments(self):
        return tournament_database.all()

    def get_one_tournament_players(self, tournament_id):
        return tournament_database.get(doc_id=tournament_id)['players']

    def get_one_tournament_matches(self, tournament_id):
        all_matches = []
        rounds = tournament_database.get(doc_id=tournament_id)['rounds']
        rounds_length = len(rounds)

        for round in rounds
            matches.append()

    def get_one_tournament_rounds(self, tournament_id):
        return tournament_database.get(doc_id=tournament_id)['rounds']
