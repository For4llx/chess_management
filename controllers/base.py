from helpers import get_rank
from tinydb.operations import add
from datetime import datetime

from controllers.player import PlayerController
from controllers.tournament import TournamentController
from models.Player import player_database

class Controller:
    def __init__(self, view):
        self.view = view
        self.player = PlayerController(view)
        self.tournament = TournamentController(view)

    def get_time_control(self):
        option = self.select_time_control()
        if option == '1':
            time_control = 'Bullet'
        elif option == '2':
            time_control = 'Blitz'
        elif option == '3':
            time_control = 'Coup rapide'
        
        return time_control
    
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

    def match_menu(self, tournament):
        tournament_rounds_number = tournament['rounds_number']
        tournament_id = tournament.doc_id
        round_index = tournament['round_index']
        match_index = tournament['match_index']
        players_id = tournament['players']
        round_counter = round_index + 1
        players = []

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
        elif match_index == tournament['rounds_number']:
            self.tournament.update_one_tournament_round_end_time(tournament_id, round_index)
            self.tournament.update_one_tournament_round_index(tournament_id)
            self.tournament.reset_one_tournament_match_index(tournament_id)
            matches = self.tournament.create_tournament_rounds_matches(players, round_counter, tournament_id)
            self.create_tournament_round(tournament_id, round_counter, matches)
            match = self.tournament.get_one_tournament_match(tournament_id, round_index, match_index)
        else:
            match = self.tournament.get_one_tournament_match(tournament_id, round_index, match_index)
        
        if match_index < tournament_rounds_number:
            while True:
                match_index = tournament['match_index']
                print(match_index)
                option = self.view.select_match_menu(match)
                if option == '1':
                    self.update_score(tournament, match)
                elif option == '0':
                    break
        else:
            self.tournament.update_one_tournament_round_end_time(tournament_id, round_index)
            self.tournament.update_one_tournament_round_index(tournament_id)
            self.tournament.reset_one_tournament_match_index(tournament_id)

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
                    self.match_menu(tournament)
                if option == '2':
                    self.select_player_menu(tournament)
                elif option == '0':
                    break
    
    def main_menu(self, view):
        while True:
            option = self.view.select_main_menu()
            if option == '1':
                self.tournament.create_tournament()
            elif option == '2':
                self.tournament_menu()
            elif option == '3':
                self.player.create_player()
            elif option == '0':
                break

    def report_menu(self, view):
        while True:
            option = self.view.select_main_menu()
            if option == '1':
                self.tournament.create_tournament()
            elif option == '2':
                self.tournament_menu()
            elif option == '3':
                self.player.create_player()
            elif option == '0':
                break