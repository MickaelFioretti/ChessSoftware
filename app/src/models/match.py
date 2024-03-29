# --- import ---
from pydantic.dataclasses import dataclass
import random

# --- models ---
from models.player import Player


@dataclass
class Match:
    """Class Matchs"""

    player1: Player = None
    score_player1: int = 0
    player2: Player = None
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
                self.winner = self.player1.name
            case 2:
                self.score_player1 = 0
                self.score_player2 = 1
                self.winner = self.player2.name
            case 3:
                self.score_player1 = 0.5
                self.score_player2 = 0.5
                self.winner = "Draw"

        self.player1.tournament_score += self.score_player1
        self.player2.tournament_score += self.score_player2

        return ([self.player1, self.score_player1], [self.player2, self.score_player2])

    def get_serialized(self):
        """Method returning the serialized match"""
        serialized_match = {
            "player1": self.player1.get_serialized(),
            "score_player1": self.score_player1,
            "player2": self.player2.get_serialized(),
            "score_player2": self.score_player2,
            "winner": self.winner,
            "name": self.name,
        }
        return serialized_match
