from pydantic.dataclasses import dataclass

# --- models ---
from models.joueur import Joueur


@dataclass
class Tours:
    """Class representing a round"""

    joueurs = list[Joueur]
    matchs = []

    def generer_matchs(self):
        """Method generating the matches of the round"""
        for i in range(0, len(self.joueurs), 2):
            self.matchs.append([self.joueurs[i], self.joueurs[i + 1]])

    generer_matchs()
