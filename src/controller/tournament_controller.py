# --- views ---
from view.menu_view import MenuView, MenuOption
from view.joueur_form_view import JoueurFormView
from view.joueur_view import JoueurView
from view.tournoi_form_view import TournoiFormView

# --- Models ---
from models.joueur import Joueur
from models.tournois import Tournois
from models.tour import Tour

# --- utils ---
from utils.clear_shell import clear_shell

"""
    ranger touts l'affichage dans les vues
    Les model ne doivent avoir que des attributs
"""


# --- Controller ---
class TournamentController:
    """Class to manage the tournament"""

    def __init__(self, menu_view: MenuView):
        self.menu_view = menu_view
        self.joueurs = [
            # Creation de joueurs par defaut 4 joueurs
            Joueur(
                first_name="Jean",
                last_name="Dupont",
                birth_date="01/01/2000",
                ranking=0,
            ),
            Joueur(
                first_name="Pierre",
                last_name="Durand",
                birth_date="01/01/2000",
                ranking=0,
            ),
            Joueur(
                first_name="Paul",
                last_name="Martin",
                birth_date="01/01/2000",
                ranking=0,
            ),
            Joueur(
                first_name="Jacques",
                last_name="Dupond",
                birth_date="01/01/2000",
                ranking=0,
            ),
        ]

    def display_menu(self):
        """Display the menu"""
        choice = self.menu_view.display()

        def user_choice(choice):
            match choice:
                case 1:
                    self.add_tournoi()
                case 2:
                    self.add_joueur()
                case 3:
                    self.display_joueurs()
                case 4:
                    self.jouer_un_tour()
                case 5:
                    self.quit()
                case _:
                    print("Choix invalide")

        user_choice(choice)

    def add_tournoi(self):
        """Add a new tournament"""
        clear_shell()
        tournoi_data = TournoiFormView().display()
        tournoi = Tournois(**tournoi_data)
        self.tournois.append(tournoi)

    def add_joueur(self):
        """Add a new player"""
        joueur_data = JoueurFormView().display()
        joueur = Joueur(**joueur_data)
        self.joueurs.append(joueur)

    def display_joueurs(self):
        """Display the players"""
        clear_shell()
        JoueurView().display(self.joueurs)
        # press enter to continue
        input("\nAppuyez sur entrée pour continuer")

    def jouer_un_tour(self):
        """Play a round"""
        clear_shell()
        print("Jouer un tour")
        # Creation d'un tour
        tour = Tour(self.joueurs)
        # generation des pairs de joueurs pour le tour

        # Affichage des matchs
        print("Matchs:")
        for match in tour.matchs:
            print(match[0].first_name, "vs", match[1].first_name)
        # press enter to continue
        input("\nAppuyez sur entrée pour continuer")

    def quit(self):
        """Quit the application"""
        exit()


# --- End Controller ---

# Creation de la vue du menu
menu_view = MenuView(
    title="Menu principal",
    options=[
        MenuOption(name="Ajouter un tournoi", value="add_tournoi"),
        MenuOption(name="Ajouter un joueur", value="add_joueur"),
        MenuOption(name="Afficher les joueurs", value="get_joueurs"),
        MenuOption(name="Jouer un tour", value="jouer_un_tour"),
        MenuOption(name="Quitter", value="quit"),
    ],
)

# Creation du controleur
controller = TournamentController(menu_view=menu_view)

# Affichage du menu et gestion des choix
while True:
    controller.display_menu()
