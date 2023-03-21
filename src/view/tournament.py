# --- view ---
from view.base_view import BaseView

# --- controller ---
from controller.timestamp import get_timestamp


# --- view ---
class CreateTournament(BaseView):
    def display_menu(self):
        date = get_timestamp()
        self.clear_shell()
        print(date + " - Création d'un nouveau tournoi")

        name = input("Entrez le nom du tournoi: \n")

        location = self.get_user_input(
            msg_display="Entrez le lieu du tournoi: \n",
            msg_error="Veuillez entrer un lieu valide",
            value_type="string",
        )

        date_debut = self.get_user_input(
            msg_display="Entrez la date de début du tournoi (jj/mm/aaaa): \n",
            msg_error="Veuillez entrer une date valide",
            value_type="date",
        )

        date_fin = self.get_user_input(
            msg_display="Entrez la date de fin du tournoi (jj/mm/aaaa): \n",
            msg_error="Veuillez entrer une date valide",
            value_type="date",
        )

        nb_players = self.get_user_input(
            msg_display="Entrez le nombre de joueurs du tournoi: \n",
            msg_error="Veuillez entrer un nombre de joueurs valide",
            value_type="numeric",
        )

        nb_rounds = self.get_user_input(
            msg_display="Entrez le nombre de rounds du tournoi: \n",
            msg_error="Veuillez entrer un nombre de rounds valide",
            value_type="numeric",
        )

        print(
            "nb_rounds :",
        )

        description = input("Entrez une description du tournoi: \n")

        return {
            "name": name,
            "location": location,
            "date_debut": date_debut,
            "date_fin": date_fin,
            "nb_players": nb_players,
            "nb_rounds": nb_rounds,
            "description": description,
        }


# --- view ---
class LoadTournament(BaseView):
    def display_menu(self):
        # TODO: load tournaments from database
        all_tournaments = []
        if all_tournaments:
            builded_selection = self.build_selection(
                iterable=all_tournaments,
                display_msg="Choisir un tournoi: \n",
                assertions=[],
            )

            user_input = int(
                self.get_user_input(
                    msg_display=builded_selection["msg"] + "\n",
                    msg_error="Veuillez entrer un nombre entier",
                    value_type="selection",
                    assertions=builded_selection["assertions"],
                )
            )

            serialized_loaded_tournament = all_tournaments[user_input - 1]

            return serialized_loaded_tournament

        else:
            return False
