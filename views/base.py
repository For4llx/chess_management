import controllers


class View:
    def select_main_menu(self):
        print('Menu principal:')
        print('1) Créer un nouveau tournoi')
        print('2) Charger un tournoi')
        print('3) Créer un nouveau joueur')
        print('4) Changer le rank d\'un joueur')
        print('5) Afficher un rapport')
        print('0) Quitter')

        return str(input())

    def select_report_menu(self):
        print('1) Afficher tout les joueurs par ordre alphabétique')
        print('2) Afficher tout les joueurs par classement')
        print(
            '3) Afficher tout les joueurs'
            'd\'un tournoi par ordre alphabétique'
        )
        print('4) Afficher tout les joueurs d\'un tournoi par classement')
        print('5) Afficher tout les tournois')
        print('6) Afficher les tour d\'un tournoi')
        print('7) Afficher les tout les matchs d\'un tournoi')
        print('0) Retour')

        return str(input())

    def select_match_menu(self, pair):
        player_1_id = pair[0][0]
        player_2_id = pair[1][0]
        print(f'Joueur {player_1_id} Contre Joueur {player_2_id}')
        print('1) Entrer les résultats du match')
        print('0) Retour')

        return str(input())

    def tournaments_list(self, tournaments):
        print('Tournois:')
        for tournament in tournaments:
            id = str(tournament.doc_id)
            name = str(tournament['name'])

            print(f'{id}) {name}')

    def rounds_list(self, rounds):
        print('Tours:')
        for round in rounds:
            name = str(round['name'])

            print(f'1) {name}')

    def matches_list(self, rounds):
        print('Tours:')
        for round in rounds:
            name = str(round['name'])
            matches = round['matches']

            print(name)

            for match in matches:
                player_1_id = str(match[0][0])
                player_1_score = str(match[0][1])
                player_2_id = str(match[1][0])
                player_2_score = str(match[1][1])

                print(f'Joueur {player_1_id} VS Joueur {player_2_id}')
                print(f'{player_1_score} | {player_2_score}')

    def select_time_control(self):
        print('Choisir un contrôle du temps:')
        print('1) Bullet')
        print('2) Blitz')
        print('3) Coup rapide')

        return str(input())

    def tournament_form(self):
        print('Créer un nouveau tournoi:')
        name = str(input('Entrer un nom:'))
        place = str(input('Entrer un lieu:'))
        rounds_number = int(input('Entrer un nombre de tours:'))
        time_control = str(controllers.tournament.TournamentController.get_time_control(self))
        description = str(input('Entrer une description:'))

        return {
            'name': name,
            'place': place,
            'rounds_number': rounds_number,
            'time_control': time_control,
            'description': description
        }

    def select_tournament(self, tournaments):
        print('Sélectionner un tournoi:')
        for tournament in tournaments:
            id = str(tournament.doc_id)
            name = str(tournament['name'])

            print(f'{id}) {name}')

        print('0) Retour')

        return str(input())

    def select_tournament_menu(self, tournament):
        print('Tournoi:' + tournament['name'])
        print('1) Continuer le tournoi')
        print('2) Ajouter un joueur membre')
        print('0) Retour')
        return str(input())

    def select_player(self, players):
        print('Sélectionner un joueur à ajouter au tournoi:')
        for player in players:
            id = str(player.doc_id)
            last_name = str(player['last_name'])
            first_name = str(player['first_name'])

            print(f'{id}) {last_name} {first_name}')

        print('0) Retour')

        return str(input())

    def select_score(self, pair):
        player_1_id = pair[0][0]
        player_2_id = pair[1][0]
        print(f'Joueur {player_1_id} Contre Joueur {player_2_id}')
        print(f'1) Joueur {player_1_id}')
        print(f'2) Joueur {player_2_id}')
        print('3) Égalité')
        print('0) Retour')

        return str(input())

    def player_form(self):
        print('Créer un nouveau joueur:')
        last_name = str(input('Entrer un nom:'))
        first_name = str(input('Entrer un prénom:'))
        birth_date = str(input('Entrer une date de naissance:'))
        sex = str(input('Choisir un sex:'))
        ranking = str(input('Entrer un classement:'))

        return {
          'last_name': last_name,
          'first_name': first_name,
          'birth_date': birth_date,
          'sex': sex,
          'ranking': ranking
        }

    def players_list(self, players):
        print('Joueurs:')
        for player in players:
            id = str(player.doc_id)
            first_name = str(player['first_name'])
            last_name = str(player['last_name'])

            print(f'{id}) {last_name} {first_name}')

    def select_sex(self):
        print('Choisir un sex:')
        print('1) Mâle')
        print('2) Femelle')

        return str(input())

    def rank_from(self):
        print('Entrer un classement:')

        return str(input())
