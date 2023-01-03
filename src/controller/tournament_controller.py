# import
from time import sleep
import os

# views
from view.menu_view import MenuView, MenuOption
from view.joueur_form_view import JoueurFormView

# Models
from models.joueur import Joueur


class TournamentController:
    """Class to manage the tournament"""

    def __init__(self, menu_view: MenuView, joueur_form_view: JoueurFormView):
        self.menu_view = menu_view
        self.joueur_form_view = joueur_form_view
        self.joueurs = []

    def display_menu(self):
        """Display the menu"""
        choice = self.menu_view.display()

        def user_choice(choice):
            match choice:
                case 1:
                    self.add_joueur()
                case 2:
                    self.display_joueurs()
                case 3:
                    self.quit()
                case _:
                    print("Choix invalide")

        user_choice(choice)

    def add_joueur(self):
        """Add a new player"""
        joueur_data = self.joueur_form_view.display()
        joueur = Joueur(**joueur_data)
        self.joueurs.append(joueur)

    def display_joueurs(self):
        """Display the players"""
        if not self.joueurs:
            os.system("cls" if os.name == "nt" else "clear")
            print("Aucun joueur")
            sleep(1)
            return
        for joueur in self.joueurs:
            print(joueur)

    def quit(self):
        """Quit the application"""
        exit()


# Creation de la vue du menu
menu_view = MenuView(
    title="Menu principal",
    options=[
        MenuOption(name="Ajouter un joueur", value="add_joueur"),
        MenuOption(name="Afficher les joueurs", value="get_joueurs"),
        MenuOption(name="Quitter", value="quit"),
    ],
)

# Creation de la vue du formulaire
joueur_form_view = JoueurFormView()

# Creation du controleur
controller = TournamentController(
    menu_view=menu_view, joueur_form_view=joueur_form_view
)

# Affichage du menu et gestion des choix
while True:
    controller.display_menu()
