# --- imports ---
from pydantic.dataclasses import dataclass
from typing import List

# --- models ---
from models.match import Match


@dataclass
class Round:
    """Class representing a round"""

    name: str
    players_pairs: List

    def create_matchs(self):
        """Method creating matchs"""
        matchs = []
        for i, pair in enumerate(self.players_paits):
            matchs.append(Match(name=f"Match {i}", players_pair=pair))
        return matchs
