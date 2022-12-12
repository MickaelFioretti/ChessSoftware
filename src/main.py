from models.Tournois import Tournois
from models.Joueurs import Joueurs


def main():
    """Main function"""

    # Create players and add them to the tournament
    player_1 = Joueurs("Dupont", "Jean", "01/01/1900", "M", 1)
    player_2 = Joueurs("Martin", "Pierre", "01/01/1900", "M", 2)
    player_3 = Joueurs("Durand", "Paul", "01/01/1900", "M", 3)
    player_4 = Joueurs("Robert", "Jacques", "01/01/1900", "M", 4)
    player_5 = Joueurs("Petit", "Marie", "01/01/1900", "F", 5)
    player_6 = Joueurs("Thomas", "Lucie", "01/01/1900", "F", 6)
    player_7 = Joueurs("Richard", "Laurent", "01/01/1900", "M", 7)
    player_8 = Joueurs("Leroy", "Julie", "01/01/1900", "F", 8)

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
