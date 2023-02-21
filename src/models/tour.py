from pydantic.dataclasses import dataclass
from typing import List

# --- models ---
from models.joueur import Joueur


@dataclass
class Tour:
    """Class representing a round"""

    joueurs: List = list[Joueur]
    matchs = []
