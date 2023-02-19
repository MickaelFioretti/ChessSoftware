from pydantic.dataclasses import dataclass
from enum import StrEnum


class SexeError(Exception):
    """Exception levée si le sexe n'est pas M ou F"""

    pass


class RankingError(Exception):
    """Exception levée si le sexe n'est pas M ou F"""

    pass


MINIMAL_RANKING_VALUE = 0
MAXIMAL_RANKING_VALUE = 1000


class Genre(StrEnum):
    """Genre d'un joueur"""

    M = "M"
    F = "F"


@dataclass
class Joueur:
    """Classe représentant un joueur de d'échecs"""

    first_name: str
    last_name: str
    birth_date: str  # format JJ/MM/AAAA
    genre: Genre  # M ou F
    ranking: int = 0  # 0 à 1000

    def __post_init__(self):
        """Méthode appelée après l'initialisation d'un joueur"""
        if self.genre not in ["M", "F"]:
            raise SexeError("Le sexe doit être M ou F")
        if self.ranking < MINIMAL_RANKING_VALUE or self.ranking > MAXIMAL_RANKING_VALUE:
            raise RankingError("Le ranking doit être compris entre 0 et 1000")

    def win(self) -> None:
        self.ranking += 1
