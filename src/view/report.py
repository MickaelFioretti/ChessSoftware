# --- Imports ---
from controller.database import load_data
from view.base_view import BaseView

from operator import itemgetter


# --- Report ---
class Report(BaseView):
    player_list = load_data()
    tournament_list = load_data()

    def display_player_report(self, player_list=[]):
        player_list = player_list

        builded_selection = self.build_selection(
            iterable=player_list,
            display_msg="Voir les details d'un joueur: \n",
            assertions=["r"],
        )

        while True:
            self.clear_shell()
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
                    self.clear_shell()
                    print(
                        f"Détails du joueur: {selected_player['first_name']} {selected_player['last_name']} \n"
                    )
                    print(
                        f"Rank: {selected_player['ranking']} \n"
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

    def display_tournament_report(self):
        builded_selection = self.build_selection(
            iterable=self.tournament_list,
            display_msg="Voir les details d'un tournoi: \n",
            assertions=["r"],
        )

        while True:
            self.clear_shell()
            print("Liste des tournois: \n")

            # --- on affiche la liste des tournois ---
            user_input = self.get_user_input(
                msg_display=builded_selection["msg"] + "r - Retour\n",
                msg_error="Veuillez entrer une option valide",
                value_type="selection",
                assertions=builded_selection["assertions"],
            )

            if user_input == "r":
                break

            else:
                selected_tournament = self.tournament_list[int(user_input) - 1]

                while True:
                    self.clear_shell()
                    print(
                        f"Détails du tournoi: {selected_tournament['name']} \n"
                        f"Lieu: {selected_tournament['location']} \n"
                        f"Date de début: {selected_tournament['date_debut']} \n"
                        f"Date de fin: {selected_tournament['date_fin']} \n"
                        f"Nombre de tours: {selected_tournament['nb_rounds']} \n"
                        f"Description: {selected_tournament['description']} \n"
                    )

                    user_input = self.get_user_input(
                        msg_display="1 - Voir les joueurs\n"
                        "2 - Voir les tours\n"
                        "r - Retour\n",
                        msg_error="Veuillez entrer une option valide",
                        value_type="selection",
                        assertions=["1", "2", "r"],
                    )

                    if user_input == "r":
                        break

                    elif user_input == "1":
                        while True:
                            user_input = self.get_user_input(
                                msg_display="Type de classement: \n"
                                "1 - Par rang\n"
                                "2 - Par ordre alphabétique\n"
                                "r - Retour\n",
                                msg_error="Veuillez entrer une option valide",
                                value_type="selection",
                                assertions=["1", "2", "r"],
                            )

                            if user_input == "r":
                                break
                            elif user_input == "1":
                                sorted_players = self.sort_player(
                                    selected_tournament, by_rank=True
                                )
                                self.display_player_report(player_list=sorted_players)
                            elif user_input == "2":
                                sorted_players = self.sort_player(
                                    selected_tournament, by_rank=False
                                )
                                self.display_player_report(player_list=sorted_players)

                    elif user_input == "2":
                        self.display_round(selected_tournament["rounds"])

    def display_round(self, rounds: list):
        builded_selection = self.build_selection(
            iterable=rounds,
            display_msg="Voir les details d'un tour: \n",
            assertions=["r"],
        )

        while True:
            self.clear_shell()
            print("Liste des tours: \n")

            # --- on affiche la liste des tournois ---
            user_input = self.get_user_input(
                msg_display=builded_selection["msg"] + "r - Retour\n",
                msg_error="Veuillez entrer une option valide",
                value_type="selection",
                assertions=builded_selection["assertions"],
            )

            if user_input == "r":
                break

            else:
                selected_round = rounds[int(user_input) - 1]

                while True:
                    self.clear_shell()
                    print(
                        f"Détails du tour: {selected_round['name']} \n"
                        f"Date de début: {selected_round['start_date']} \n"
                        f"Date de fin: {selected_round['end_date']} \n"
                        f"Nombre de matchs: {selected_round['nb_matchs']} \n"
                    )

                    user_input = self.get_user_input(
                        msg_display="1 - Voir les matchs\n" "r - Retour\n",
                        msg_error="Veuillez entrer une option valide",
                        value_type="selection",
                        assertions=["1", "r"],
                    )

                    if user_input == "r":
                        break

                    elif user_input == "1":
                        builded_selection = self.build_selection(
                            iterable=selected_round["matchs"],
                            display_msg="Voir les details d'un match: \n",
                            assertions=["r"],
                        )
                        print("Liste des matchs: \n")
                        user_input = self.get_user_input(
                            msg_display=builded_selection["msg"] + "r - Retour\n",
                            msg_error="Veuillez entrer une option valide",
                            value_type="selection",
                            assertions=builded_selection["assertions"],
                        )

                        if user_input == "r":
                            break
                        else:
                            selected_match = selected_round["matchs"][
                                int(user_input) - 1
                            ]
                            while True:
                                self.clear_shell()
                                print(
                                    f"Détails du match: {selected_match['name']} \n"
                                    f"Joueur 1: {selected_match['player_1']['last_name']}"
                                    + f"{selected_match['player_1']['first_name']} \n"
                                    f"Joueur 2: {selected_match['player_2']['last_name']}"
                                    + "{selected_match['player_2']['first_name']} \n"
                                    f"Gagnant: {selected_match['winner']} \n"
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
            sorted_players = sorted(players["players"], key=itemgetter("ranking"))
        else:
            sorted_players = sorted(players["players"], key=itemgetter("last_name"))

        return sorted_players
