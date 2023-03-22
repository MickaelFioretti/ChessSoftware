# --- import ---
from pydantic.dataclasses import dataclass
from pydantic.fields import Field
from typing import List


@dataclass
class Player:
    """Classe représentant un joueur d'échecs"""

    first_name: str
    last_name: str
    birth_date: str
    ranking: int = 0
    total_score: int = 0
    tournament_score: int = 0
    played_with: List[str] = Field(default_factory=list)

    def get_serialized_player(self):
        """Méthode retournant le joueur sérialisé"""
        serialized_player = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birth_date": self.birth_date,
            "ranking": self.ranking,
            "total_score": self.total_score,
            "tournament_score": self.tournament_score,
            "played_with": self.played_with,
        }
        return serialized_player
