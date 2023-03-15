# --- PIP ---
from pydantic.dataclasses import dataclass
from typing import List

# --- LOCAL ---
from utils.clear_shell import clear_shell

# --- CONTROLLER ---
from controller.player import update_ranking
from controller.tournament import create_tournament, play_tournament

# --- View ---
from view.base import BaseView
from view.player import CreatePlayer


@dataclass
class MenuOption:
    """Class to represent a menu option"""

    name: str
    value: str


@dataclass
class MenuView:
    """Class to display a menu and handle user input"""

    title: str
    options: List[MenuOption]

    def display(self):
        """Display the menu"""
        clear_shell()
        print(self.title)
        print()
        for i, option in enumerate(self.options):
            print(f"{i + 1} - {option.name}")
        print()
        choice = input("Choisissez une option: ")
        return int(choice)


@dataclass
class MainMenu(BaseView):
    def display_main_menu(self):
        while True:
            clear_shell()
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
                clear_shell()
                user_input = self.get_user_input(
                    msg_display="Nombre de joueurs a créer:\n",
                    msg_error="Veuillez entrer un nombre valide",
                    value_type="numeric",
                )
                for i in range(user_input):
                    serialized_player = CreatePlayer().display_menu()
                    print(serialized_player)
                    # TODO: save player

            # --- on affiche les rapports ---
            elif user_input == "4":
                while True:
                    clear_shell()
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
                            clear_shell()
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
                                pass
                            elif user_input == "2":
                                pass

                    elif user_input == "2":
                        pass

            else:
                quit()

        # on joue le tournoi
        clear_shell()
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
        clear_shell()
        print(f"Tournoir {tournament.name} terminé !\n Résultats:")
        for i, player in enumerate(rankings):
            print(f"{str(i + 1)} - {player}")

        # --- on met a jour les classements ---
        clear_shell()
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
                clear_shell()
                rank = self.get_user_input(
                    msg_display=f"Classement de {player.name}:\n",
                    msg_error="Veuillez entrer un nombre valide",
                    value_type="numeric",
                )
                update_ranking(player, rank)

        else:
            quit()
