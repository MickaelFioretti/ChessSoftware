from pydantic.dataclasses import dataclass
from typing import List

from .joueur import Joueur
from .tour import Tour


@dataclass
class Tournoi:
    """Class representing a tournament"""

    name: str
    location: str
    date_debut: str
    date_fin: str
    nombre_de_tours: int = 4
    numero_tour_actuel: int = 1
    tours: List[Tour] = list[Tour]
    joueurs: List[Joueur] = list[Joueur]
    description: str = ""

    def add_player(self, player):
        """Method adding a player to the tournament"""
        self.joueurs.append(player)

    def add_tour(self, tour: Tour):
        """Method adding a round to the tournament"""
        self.tours.append(tour)
