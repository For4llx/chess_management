from helpers import get_rank
from datetime import datetime

from models.Tournament import Tournament, tournament_database
from models.Player import player_database
from models.Round import Round

from views.base import View


class TournamentController:
    def __init__(self):
        self.view = View()

    def create_tournament(self):
        tournament = self.view.tournament_form()
        tournament = Tournament(
            tournament['name'],
            tournament['place'],
            tournament['time_control'],
            tournament['description'],
            tournament['rounds_number'])
        tournament.save()

    def create_tournament_round(self, tournament_id, round_counter, matches):
        round = Round(f'Round {round_counter}', matches)
        rounds = tournament_database.get(doc_id=tournament_id)['rounds']
        rounds.append(round.__dict__)
        tournament_database.update({'rounds': rounds}, doc_ids=[tournament_id])

    def create_tournament_rounds_matches(self, players, round_counter, tournament_id):
        if round_counter == 1:
            matches = []
            players.sort(key=get_rank)
            players_number = len(players)
            middle_index = players_number // 2
            upper_class_players = players[:middle_index]
            lower_class_players = players[middle_index:]

            for upper_class_player, lower_class_player in zip(upper_class_players, lower_class_players):
                player_1_id = upper_class_player.doc_id
                player_2_id = lower_class_player.doc_id
                matches.append([[player_1_id, 0], [player_2_id, 0]])

            return matches
        else:
            matches = []
            players = sorted(players, key=lambda x: (x['points'], x['ranking']))

            while len(players) != 0:
                first_player = players.pop(0)
                for player in players:
                    if player.doc_id not in first_player['opponents']:
                        second_player = player
                        matches.append([[first_player.doc_id, 0], [second_player.doc_id, 0]])
                        players.remove(player)
                        break
            
            return matches

    def get_all_tournaments(self):
        return tournament_database.all()

    def get_one_tournament(self, tournament_id):
        return tournament_database.get(doc_id=tournament_id)
    
    def get_tournament_players(self, tournament_id):
        return tournament_database.get(doc_id=tournament_id)['players']
    
    def get_one_tournament_rounds(self, tournament_id):
        return tournament_database.get(doc_id=tournament_id)['rounds']

    def get_one_tournament_match(self, tournament_id, round_index, match_index):
        return tournament_database.get(doc_id=tournament_id)['rounds'][round_index]['matches'][match_index]

    def get_one_tournament_players(self, tournament_id):
        players = []
        players_id = tournament_database.get(doc_id=tournament_id)['players']
        for player_id in players_id:
            players.append(player_database.get(doc_id=player_id))
        
        return players

    def update_one_tournament_match_index(self, tournament_id, match_index):
        match_index = tournament_database.get(doc_id=tournament_id)['match_index']
        match_index = match_index + 1
        tournament_database.update({'match_index': match_index}, doc_ids=[tournament_id])
    
    def reset_one_tournament_match_index(self, tournament_id):
        tournament_database.update({'match_index': 0}, doc_ids=[tournament_id])
    
    def update_one_tournament_round_end_time(self, tournament_id, round_index):
        rounds = tournament_database.get(doc_id=tournament_id)['rounds']
        rounds[round_index]['end_time'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        tournament_database.update({'rounds': rounds}, doc_ids=[tournament_id])

    def update_one_tournament_players(self, tournament_id, player_id):
        players = tournament_database.get(doc_id=tournament_id)['players']
        players.append(player_id)
        tournament_database.update({'players': players}, doc_ids=[tournament_id])

    def update_one_tournament_rounds(self, tournament_id, round):
        rounds = tournament_database.get(doc_id=tournament_id)['rounds']
        rounds.append(round)
        tournament_database.update({'rounds': rounds}, doc_ids=[tournament_id])
  
    def update_one_tournament_current_round(self, tournament_id):
        current_round = tournament_database.get(doc_id=tournament_id)['current_round']
        current_round = current_round + 1
        tournament_database.update({'current_round': current_round}, doc_ids=[tournament_id])
    
    def update_one_tournament_current_matches(self, tournament_id, match):
        current_matches = tournament_database.get(doc_id=tournament_id)['current_matches']
        current_matches.append(match)
        tournament_database.update({'current_matches': current_matches}, doc_ids=[tournament_id])
      
    def update_one_tournament_player_score(self, tournament_id, player, score, round_index, match_index):
        rounds = tournament_database.get(doc_id=tournament_id)['rounds']
        rounds[round_index]['matches'][match_index][player][1] = score
        tournament_database.update({'rounds': rounds}, doc_ids=[tournament_id])

    def update_one_tournament_rounds(self, tournament_id, round):
        rounds = tournament_database.get(doc_id=tournament_id)['rounds']
        rounds.append(round.__dict__)
        tournament_database.update({'rounds': rounds}, doc_ids=[tournament_id])

    def update_one_tournament_round_index(self, tournament_id):
        round_index = tournament_database.get(doc_id=tournament_id)['round_index']
        round_index = round_index + 1
        tournament_database.update({'round_index': round_index}, doc_ids=[tournament_id])

    def update_score(self, tournament, match):
        tournament_id = tournament.doc_id
        players = tournament['players']
        match_index = tournament['match_index']
        round_index = tournament['round_index']
        player_1 = match[0]
        player_2 = match[1]

        option = self.view.select_score(match)

        if option == '1':
            match = [[player_1, 1],[player_2, 0]]
            self.tournament.update_one_tournament_player_score(tournament_id, 0, 1, round_index, match_index)
            self.player.update_one_tournament_player_point(player_1[0], 1)
            self.tournament.update_one_tournament_match_index(tournament_id, match_index)
        elif option == '2':
            match = [[player_1, 0],[player_2, 1]]
            self.tournament.update_one_tournament_player_score(tournament_id, 1, 1, round_index, match_index)
            self.player.update_one_tournament_player_point(player_2[0], 1)
            self.tournament.update_one_tournament_match_index(tournament_id, match_index)
        elif option == '3':
            match = [[player_1, 0.5],[player_2, 0.5]]
            self.tournament.update_one_tournament_player_score(tournament_id, 0, 0.5, round_index, match_index)
            self.tournament.update_one_tournament_player_score(tournament_id, 1, 0.5, round_index, match_index)
            self.player.update_one_tournament_player_point(player_1[0], 0.5)
            self.player.update_one_tournament_player_point(player_2[0], 0.5)
            self.tournament.update_one_tournament_match_index(tournament_id, match_index)
    
    def random_color(self):
        colors = ['Black', 'White']
        color_1 = choice(colors)
        colors.remove(color_1)
        color_2 = colors[0]
        print(color_1)
        print(color_2)

    def get_time_control(self):
        option = self.select_time_control()
        if option == '1':
            time_control = 'Bullet'
        elif option == '2':
            time_control = 'Blitz'
        elif option == '3':
            time_control = 'Coup rapide'
        
        return time_control