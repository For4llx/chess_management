from controllers.base import Controller

class View:
    def select_main_menu(self):
        print('Menu principal:')
        print('1) Créer un nouveau tournoi')
        print('2) Charger un tournoi')
        print('3) Créer un nouveau joueur')
        print('4) Afficher un rapport')
        print('0) Quitter')

        return str(input())

    def select_report_menu(self):
        print('1) Afficher tout les joueurs')
        print('2) Afficher tout les joueurs d\'un tournoi')
        print('1) Afficher tout les tournoi')
        print('1) Afficher les tour d\'un tournoi')
        print('1) Afficher les tout les matchs d\'un tournoi')

        return str(input())

    def select_time_control(self):
        print('Choisir un contrôle du temps:')
        print('1) Bullet')
        print('2) Blitz')
        print('3) Coup rapide')

        return str(input())
    
    def select_sex(self):
        print('Choisir un sex:')
        print('1) Mâle')
        print('2) Femelle')

        return str(input())

    def tournament_form(self):
        print('Créer un nouveau tournoi:')
        name = str(input('Entrer un nom:'))
        place = str(input('Entrer un lieu:'))
        rounds_number = int(input('Entrer un nombre de tours:'))
        time_control = str(Controller.get_time_control(self))
        description = str(input('Entrer une description:'))

        return {
            'name': name,
            'place': place,
            'rounds_number': rounds_number,
            'time_control': time_control,
            'description': description
        }
    
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

    def select_match_menu(self, pair):
        player_1_id = pair[0][0]
        player_2_id = pair[1][0]
        print(f'Joueur {player_1_id} Contre Joueur {player_2_id}')
        print('1) Entrer les résultats du match')
        print('0) Retour')

        return str(input())

    def select_score(self, pair):
        player_1_id = pair[0][0]
        player_2_id = pair[1][0]
        print(f'Joueur {player_1_id} Contre Joueur {player_2_id}')
        print(f'1) Joueur {player_1_id}')
        print(f'2) Joueur {player_2_id}')
        print(f'3) Égalité')
        print('0) Retour')

        return str(input())
