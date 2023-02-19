from pydantic.dataclasses import dataclass
from typing import List

from .matchs import Matchs
from .joueur import Joueur
from .tours import Tours


@dataclass
class Tournois:
    """Class representing a tournament"""

    name: str
    location: str
    date_debut: str
    date_fin: str
    nombre_de_tours: int = 4
    numero_tour_actuel: int = 1
    tours: List[Matchs]
    joueurs: List[Joueur]
    description: str

    def add_player(self, player):
        """Method adding a player to the tournament"""
        self.joueurs.append(player)

    def add_tour(self, tour: Tours):
        """Method adding a round to the tournament"""
        self.tours.append(tour)

    def classement_final(self):
        """Method returning the final ranking of the tournament"""
        classement = {}
        for tour in self.tours:
            for match in tour.matchs:
                joueur1, joueur2 = match[0][0], match[1][0]
                score1, score2 = match[0][1], match[1][1]
                if joueur1 not in classement:
                    classement[joueur1] = joueur1.ranking
                if joueur2 not in classement:
                    classement[joueur2] = joueur2.ranking
                classement[joueur1] += score1
                classement[joueur2] += score2
            return sorted(classement.items(), key=lambda x: x[1], reverse=True)
