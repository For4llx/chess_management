from models.Player import Player, player_database

class PlayerController:
    def __init__(self, view):
        self.view = view

    def create_player(self):
        player = self.view.player_form()
        player = Player(
            player['last_name'],
            player['first_name'],
            player['ranking'],
            player['birth_date'],
            player['sex'])
        player.save()

    def update_one_player_opponents(self, player_id, opponent):
        opponents = player_database.get(doc_id=player_id)['opponents']
        opponents.append(opponent)
        player_database.update({'opponents': opponents}, doc_ids=[player_id])

    def update_one_tournament_player_point(self, player_id, score):
        points = player_database.get(doc_id=player_id)['points']
        points = points + score
        player_database.update({'points': points}, doc_ids=[player_id])

    def get_all_players(self):
        return player_database.all()
    
    def get_one_player(self, player_id):
        return player_database.get(doc_id=player_id)