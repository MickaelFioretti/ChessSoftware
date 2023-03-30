# --- import ---
from pydantic.dataclasses import dataclass
from pydantic.fields import Field
from typing import List


@dataclass
class Player:
    """Classe représentant un joueur d'échecs"""

    first_name: str
    name: str
    birth_date: str
    ranking: int = 0
    total_score: int = 0
    tournament_score: int = 0
    played_with: List[str] = Field(default_factory=list)

    def get_serialized(self):
        """Méthode retournant le joueur sérialisé"""
        serialized_player = {
            "first_name": self.first_name,
            "name": self.name,
            "birth_date": self.birth_date,
            "ranking": self.ranking,
            "total_score": self.total_score,
            "tournament_score": self.tournament_score,
        }
        return serialized_player
