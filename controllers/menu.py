from helpers import get_rank

from views.base import View

from controllers.player import PlayerController
from controllers.tournament import TournamentController


class MenuController:
    def __init__(self):
        self.view = View()

        self.player = PlayerController()
        self.tournament = TournamentController()

    def report_menu(self):
        all_players = self.player.get_all_players()
        all_tournaments = self.tournament.get_all_tournaments()
        while True:
            option = self.view.select_report_menu()
            if option == '1':
                all_players = sorted(all_players, key=lambda x: (x['last_name'], x['first_name']))
                self.view.players_list(all_players)
            elif option == '2':
                all_players.sort(key=get_rank)
                self.view.players_list(all_players)
            elif option == '3':
                tournament_id = self.view.select_tournament(all_tournaments)
                tournament_players = self.tournament.get_one_tournament_players(tournament_id)
                tournament_players = sorted(all_players, key=lambda x: (x['last_name'], x['first_name']))
                self.view.players_list(tournament_players)
            elif option == '4':
                tournament_id = self.view.select_tournament(all_tournaments)
                tournament_players = self.tournament.get_one_tournament_players(tournament_id)
                tournament_players.sort(key=get_rank)
                self.view.players_list(tournament_players)
            elif option == '5':
                self.view.tournaments_list(all_tournaments)
            elif option == '6':
                tournament_id = self.view.select_tournament(all_tournaments)
                tournament_rounds = self.tournament.get_one_tournament_rounds(tournament_id)
                self.view.rounds_list(tournament_rounds)
            elif option == '7':
                tournament_id = self.view.select_tournament(all_tournaments)
                tournament_rounds = self.tournament.get_one_tournament_rounds(tournament_id)
                self.view.matches_list(tournament_rounds)
            elif option == '0':
                break

    def main_menu(self):
        while True:
            option = self.view.select_main_menu()
            if option == '1':
                self.tournament.create_tournament()
            elif option == '2':
                self.tournament_menu()
            elif option == '3':
                self.player.create_player()
            elif option == '4':
                all_players = self.player.get_all_players()
                player_id = self.view.select_player(all_players)
                player_id = int(player_id)
                ranking = self.view.rank_from()
                self.player.update_one_player_rank(player_id, ranking)
            elif option == '5':
                self.report_menu(view)
            elif option == '0':
                break
    
    def match_menu(self, tournament_id):
        while True:
            tournament = self.tournament.get_one_tournament(tournament_id)
            tournament_rounds_number = tournament['rounds_number']
            tournament_id = tournament.doc_id
            round_index = tournament['round_index']
            match_index = tournament['match_index']
            players_id = tournament['players']
            round_counter = round_index + 1
            players = []
            
            if match_index == 4:
                print('test')
                self.tournament.update_one_tournament_round_end_time(tournament_id, round_index)
                self.tournament.update_one_tournament_round_index(tournament_id)
                self.tournament.reset_one_tournament_match_index(tournament_id)
                tournament = self.tournament.get_one_tournament(tournament_id)
                round_index = tournament['round_index']
                match_index = tournament['match_index']
                round_counter = round_counter + 1
                print(round_counter)

            if round_counter <= tournament_rounds_number:
                if match_index == 0:
                    for player_id in players_id:
                        players.append(player_database.get(doc_id=player_id))
                
                    matches = self.tournament.create_tournament_rounds_matches(players, round_counter, tournament_id)
                    for match in matches:
                        player_1 = match[0][0]
                        player_2 = match[1][0]
                        self.player.update_one_player_opponents(player_1, player_2)
                        self.player.update_one_player_opponents(player_2, player_1)

                    self.tournament.create_tournament_round(tournament_id, round_counter, matches)

                match = self.tournament.get_one_tournament_match(tournament_id, round_index, match_index)                
                option = self.view.select_match_menu(match)
                if option == '1':
                    self.update_score(tournament, match)
                elif option == '0':
                    break
            else:
                round_index = round_index - 1
                self.tournament.update_one_tournament_round_end_time(tournament_id, round_index)
                self.tournament.reset_one_tournament_match_index(tournament_id)
                break

    def tournament_menu(self):
        all_tournaments = self.tournament.get_all_tournaments()

        while True:
            option = self.view.select_tournament(all_tournaments)
            if option == '0':
                break
            else:
                tournament_id = option
                tournament_id = int(tournament_id)
                tournament = self.tournament.get_one_tournament(tournament_id)

            while True:
                option = self.view.select_tournament_menu(tournament)
                if option == '1':
                    self.match_menu(tournament.doc_id)
                if option == '2':
                    self.select_player_menu(tournament)
                elif option == '0':
                    break

    def select_player_menu(self, tournament):
        all_players = self.player.get_all_players()
        tournament_id = tournament.doc_id

        while True:
            option = self.view.select_player(all_players)
            if option == '0':
                break
            else:
                player_id = option
                player_id = int(player_id)
            
            self.tournament.update_one_tournament_players(tournament_id, player_id)