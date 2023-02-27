# --- import ---
from pydantic.dataclasses import dataclass
from typing import List


@dataclass
class Match:
    """Class Matchs"""

    score_player1: int = 0
    score_player2: int = 0
    winner: str = ""
    name: str = ""

    def __init__(self, player_pair: List[str]) -> None:
        """Method initializing a match"""
        self.player1 = player_pair[0]
        self.player2 = player_pair[1]
