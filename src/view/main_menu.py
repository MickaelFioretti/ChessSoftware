# --- PIP ---
from pydantic.dataclasses import dataclass

# --- CONTROLLER ---
from controller.player import update_ranking
from controller.tournament import create_tournament, play_tournament
from controller.database import save_data

# --- View ---
from view.base_view import BaseView
from view.player import CreatePlayer
from view.report import Report


@dataclass
class MainMenu(BaseView):
    def display_main_menu(self):
        while True:
            self.clear_shell()
            user_input = self.get_user_input(
                msg_display="Choisissez une option: \n"
                "1 - Créer un nouveau tournoi\n"
                "2 - Charger un tournoi\n"
                "3 - Créer des joueurs\n"
                "4 - Voir les rapports\n"
                "q - Quitter\n",
                msg_error="Veuillez entrer une option valide",
                value_type="selection",
                assertions=["1", "2", "3", "4", "q"],
            )

            # --- on cree un nouveau tournoi ---
            if user_input == "1":
                tournament = create_tournament()
                break

            # --- on charge un tournoi ---
            # TODO: load tournament
            elif user_input == "2":
                pass

            # --- on cree des joueurs ---
            elif user_input == "3":
                self.clear_shell()
                user_input = self.get_user_input(
                    msg_display="Nombre de joueurs a créer:\n",
                    msg_error="Veuillez entrer un nombre valide",
                    value_type="numeric",
                )
                for i in range(user_input):
                    serialized_player = CreatePlayer().display_menu()
                    # TODO: save player
                    save_data("players", serialized_player)

            # --- on affiche les rapports ---
            elif user_input == "4":
                while True:
                    self.clear_shell()
                    user_input = self.get_user_input(
                        msg_display="Choisissez une option: \n"
                        "1 - Rapport des joueurs\n"
                        "2 - Rapport des tournois\n"
                        "r - Retour\n",
                        msg_error="Veuillez entrer une option valide",
                        value_type="selection",
                        assertions=["1", "2", "r"],
                    )
                    if user_input == "r":
                        break
                    elif user_input == "1":
                        while True:
                            self.clear_shell()
                            user_input = self.get_user_input(
                                msg_display="Voir le classement par:\n"
                                "1 - Rang\n"
                                "2 - Ordre alphabétique\n"
                                "r - Retour\n",
                                msg_error="Veuillez entrer une option valide",
                                value_type="selection",
                                assertions=["1", "2", "r"],
                            )
                            if user_input == "r":
                                break
                            elif user_input == "1":
                                self.clear_shell()
                                sorted_players = Report().sort_player(
                                    Report().player_list, by_rank=True
                                )
                                Report().display_player_report(
                                    player_list=sorted_players
                                )
                            elif user_input == "2":
                                self.clear_shell()
                                sorted_players = Report().sort_player(
                                    Report().player_list, by_rank=False
                                )
                                Report().display_player_report(
                                    player_list=sorted_players
                                )

                    elif user_input == "2":
                        pass

            else:
                quit()

        # on joue le tournoi
        self.clear_shell()
        user_input = self.get_user_input(
            msg_display="Que voulez-vous faire ?\n"
            "1 - Jouer le tournoi\n"
            "q - Quitter\n",
            msg_error="Veuillez entrer une option valide",
            value_type="selection",
            assertions=["1", "q"],
        )

        # --- on recupere les resultats une fois le tournoi fini ---
        if user_input == "1":
            rankings = play_tournament(tournament, new_tournament_loaded=True)
        else:
            quit()

        # --- on affiche le classement ---
        self.clear_shell()
        print(f"Tournoir {tournament.name} terminé !\n Résultats:")
        for i, player in enumerate(rankings):
            print(f"{str(i + 1)} - {player}")

        # --- on met a jour les classements ---
        self.clear_shell()
        user_input = self.get_user_input(
            msg_display="Mise a jour des classements:\n"
            "1 - Automatiquement\n"
            "2 - Manuellement\n"
            "q - Quitter\n",
            msg_error="Veuillez entrer une option valide",
            value_type="selection",
            assertions=["1", "2", "q"],
        )
        if user_input == "1":
            for i, player in enumerate(rankings):
                print(player.name)
                update_ranking(player, i + 1)

        elif user_input == "2":
            for player in rankings:
                self.clear_shell()
                rank = self.get_user_input(
                    msg_display=f"Classement de {player.name}:\n",
                    msg_error="Veuillez entrer un nombre valide",
                    value_type="numeric",
                )
                update_ranking(player, rank)

        else:
            quit()
