from pydantic.dataclasses import dataclass
from enum import StrEnum


class Sexe(StrEnum):
    """Enum représentant le sexe d'un joueur"""

    M = "M"
    F = "F"


@dataclass
class Joueur:
    """Classe représentant un joueur d'échecs"""

    first_name: str
    last_name: str
    birth_date: str
    sexe: Sexe
    ranking: int = 0
