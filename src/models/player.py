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
