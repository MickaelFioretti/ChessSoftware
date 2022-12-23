from typing import List
from .matchs import Matchs
from .joueur import Joueur


class Tournois:
    """Class representing a tournament"""

    def __init__(
        self,
        name: str,
        location: str,
        date: str,
        tours: List[Matchs],
        joueurs: List[Joueur],
        time_control: str,
        description: str,
        number_of_rounds: int = 4,
    ):
        """Constructor"""
        self.name = name
        self.location = location
        self.date = date
        self.number_of_rounds = number_of_rounds
        self.tours = tours
        self.joueurs = joueurs
        self.time_control = time_control
        self.description = description

    def add_player(self, player):
        """Method adding a player to the tournament"""
        self.joueurs.append(player)

    def __str__(self):
        """Method returning tournament information"""
        return f"""
                Nom du tournoi : {self.name}\n
                Lieu : {self.location}\n
                Date : {self.date}\n
                Nombre de tours : {self.number_of_rounds}\n
                Liste des joueurs : {self.joueurs}\n
                Contrôle du temps : {self.time_control}\n
                Description : {self.description}
            """

    def play_round(self):
        """Method playing a round"""
        # generate pair
        # joue le resultat des pairs
        # en fonction du résultat
        # joueur1.defeat ou joueur1.win et joueur2.defeat ou joueur2.win

    def __repr__(self):
        return str(self)
