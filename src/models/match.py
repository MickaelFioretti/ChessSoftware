# --- import ---
from pydantic.dataclasses import dataclass
from typing import List
import random

# --- models ---
from models.player import Player


@dataclass
class Match:
    """Class Matchs"""

    players_pair: List[Player] = []
    player1: str = players_pair[0]
    score_player1: int = 0
    player2: str = players_pair[1]
    score_player2: int = 0
    winner: str = ""
    name: str = ""

    def play_match(self) -> None:
        """Method playing a match"""
        winner = random.choice([1, 2, 3])

        # --- match winner ---
        match winner:
            case 1:
                self.score_player1 = 1
                self.score_player2 = 0
                self.winner = self.player1.first_name
            case 2:
                self.score_player1 = 0
                self.score_player2 = 1
                self.winner = self.player2.first_name
            case 3:
                self.score_player1 = 0.5
                self.score_player2 = 0.5
                self.winner = "Draw"

        self.player1.tournament_score += self.score_player1
        self.player2.tournament_score += self.score_player2
