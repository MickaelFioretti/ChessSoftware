from pydantic.dataclasses import dataclass
from typing import List

from .matchs import Matchs
from .joueur import Joueur


@dataclass
class Tournois:
    """Class representing a tournament"""

    name: str
    location: str
    date: str
    number_of_rounds: int = 4
    tours: List[Matchs] = []
    joueurs: List[Joueur] = []
    time_control: str = "bullet"
    description: str = "aucune description"

    def add_player(self, player):
        """Method adding a player to the tournament"""
        self.joueurs.append(player)

    def play_round(self):
        """Method playing a round"""
        # generate pair
        # joue le resultat des pairs
        # en fonction du résultat
        # joueur1.defeat ou joueur1.win et joueur2.defeat ou joueur2.win
