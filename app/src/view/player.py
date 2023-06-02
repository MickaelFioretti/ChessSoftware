from view.base_view import BaseView
from controller.database import load_data


class CreatePlayer(BaseView):
    def display_menu(self):
        self.clear_shell()

        name = input("Entrez le nom du joueur: ")

        first_name = input("Entrez le prénom du joueur: ")

        birth_date = self.get_user_input(
            msg_display="Entrez la date de naissance du joueur (jj/mm/aaaa): ",
            msg_error="Veuillez entrer une date valide",
            value_type="date",
        )

        ranking = self.get_user_input(
            msg_display="Entrez le classement du joueur (0 a 1000): ",
            msg_error="Veuillez entrer un classement valide",
            value_type="numeric",
        )

        print(f"Le joueur {first_name} {name} a bien été créé")

        return {
            "first_name": first_name,
            "name": name,
            "birth_date": birth_date,
            "ranking": ranking,
            "total_score": 0,
        }


class LoadPlayer(BaseView):
    def display_menu(self, nb_players_to_load):
        all_players = load_data()["players"]
        serialized_players = []
        for i in range(nb_players_to_load):
            print(f"Plus que {nb_players_to_load - i} joueurs a charger")
            display_msg = "Entrez le nom du joueur: \n"

            assertions = []
            for i, player in enumerate(all_players):
                display_msg += f"{i + 1} - {player['name']} {player['first_name']}\n"
                assertions.append(str(i + 1))

            user_input = int(
                self.get_user_input(
                    msg_display=display_msg,
                    msg_error="Veuillez entrer un nom valide",
                    value_type="selection",
                    assertions=assertions,
                )
            )
            if all_players[user_input - 1] not in serialized_players:
                serialized_players.append(all_players[user_input - 1])
            else:
                print("Ce joueur a déjà été chargé")
                nb_players_to_load += 1

        return serialized_players
