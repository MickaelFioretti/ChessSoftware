# --- Imports ---
from controller.database import load_data
from view.base_view import BaseView
from operator import itemgetter


# --- Report ---
class Report(BaseView):
    player_list = load_data("players")
    tournament_list = load_data("tournaments")

    def display_player_report(self, player_list=[]):
        player_list = player_list

        builded_selection = self.build_selection(
            iterable=player_list,
            display_msg="Voir les details d'un joueur: \n",
            assertions=["r"],
        )

        while True:
            print("Classement des joueurs: \n")

            user_input = self.get_user_input(
                msg_display=builded_selection["msg"] + "r - Retour\n",
                msg_error="Veuillez entrer une option valide",
                value_type="selection",
                assertions=builded_selection["assertions"],
            )

            if user_input == "r":
                break

            else:
                selected_player = player_list[int(user_input) - 1]

                while True:
                    print(
                        f"Détails du joueur: {selected_player['first_name']} {selected_player['last_name']} \n"
                    )
                    print(
                        f"Rank: {selected_player['ranking']} \n"
                        f"Score: {selected_player['score']} \n"
                        f"Score total: {selected_player['total_score']} \n"
                        f"Date de naissance: {selected_player['birth_date']} \n"
                    )

                    user_input = self.get_user_input(
                        msg_display="r - Retour\n",
                        msg_error="Veuillez entrer une option valide",
                        value_type="selection",
                        assertions=["r"],
                    )

                    if user_input == "r":
                        break

    @staticmethod
    def sort_player(players: list, by_rank: bool) -> list:
        if by_rank:
            sorted_players = sorted(players, key=itemgetter("ranking"))
        else:
            sorted_players = sorted(players, key=itemgetter("last_name"))

        return sorted_players
