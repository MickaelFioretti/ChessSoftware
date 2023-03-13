# --- PIP ---
from pydantic.dataclasses import dataclass
from typing import List

# --- LOCAL ---
from utils.clear_shell import clear_shell

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
            print()
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
                self.create_tournament()
                break

            # --- on charge un tournoi ---
            elif user_input == "2":
                pass

            # --- on cree des joueurs ---
            elif user_input == "3":
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
        print()
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
            ranking = self.play_tournament()
            print(ranking)
            # TODO: save tournament
        else:
            quit()
