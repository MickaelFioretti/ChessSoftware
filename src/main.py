from models.joueur import Joueur
from models.tournois import Tournois


def main():
    """Main function"""

    # Create players and add them to the tournament
    player_1 = Joueur("Dupont", "Jean", "01/01/1900", "M", 1)
    player_2 = Joueur("Martin", "Pierre", "01/01/1900", "M", 2)
    player_3 = Joueur("Durand", "Paul", "01/01/1900", "M", 3)
    player_4 = Joueur("Robert", "Jacques", "01/01/1900", "M", 4)
    player_5 = Joueur("Petit", "Marie", "01/01/1900", "F", 5)
    player_6 = Joueur("Thomas", "Lucie", "01/01/1900", "F", 6)
    player_7 = Joueur("Richard", "Laurent", "01/01/1900", "M", 7)
    player_8 = Joueur("Leroy", "Julie", "01/01/1900", "F", 8)

    # Create tournament
    tournament = Tournois(
        "Tournoi de test", "Paris", "01/01/2020", [], [], "Blitz", "Test"
    )

    # Add players to the tournament
    tournament.add_player(player_1)
    tournament.add_player(player_2)
    tournament.add_player(player_3)
    tournament.add_player(player_4)
    tournament.add_player(player_5)
    tournament.add_player(player_6)
    tournament.add_player(player_7)
    tournament.add_player(player_8)

    # Display tournament information
    print(tournament)


if __name__ == "__main__":
    main()
