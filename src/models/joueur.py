from pydantic.dataclasses import dataclass


@dataclass
class Joueur:
    """Classe représentant un joueur d'échecs"""

    first_name: str
    last_name: str
    birth_date: str
    ranking: int = 0

    def add_points(self, points: int):
        """Méthode ajoutant des points au classement du joueur"""
        self.ranking += points
