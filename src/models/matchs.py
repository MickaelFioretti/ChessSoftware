from pydantic.dataclasses import dataclass


@dataclass
class Matchs:
    """Class Matchs"""

    joueur1: str
    joueur2: str
    joueur1_score: int
    joueur2_score: int
