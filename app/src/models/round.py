# --- imports ---
from pydantic.dataclasses import dataclass
import dataclasses
from typing import List, Tuple

# --- models ---
from models.match import Match
from models.player import Player

# --- controller ---
from controller.timestamp import get_timestamp


@dataclass
class Round:
    """Class representing a round"""

    name: str
    players_pair: List[Tuple[Player, Player]] = dataclasses.field(default_factory=list)
    start_date: str = get_timestamp()
    end_date: str = ""
    load_matchs: bool = False
    matchs: List[Match] = dataclasses.field(default_factory=list)

    def __post_init__(self):
        if self.load_matchs:
            self.matchs = []
        else:
            self.matchs = self.create_matchs()

    def create_matchs(self):
        """Method creating matchs"""
        matchs = []
        for i, pair in enumerate(self.players_pair):
            matchs.append(Match(name=f"Match {i}", player1=pair[0], player2=pair[1]))
        return matchs

    def play_round(self):
        self.end_date = get_timestamp()
        print(f"Fin du {self.name} le {self.end_date}")
        print("Resultats des matchs:")
        for match in self.matchs:
            match.play_match()
            print(
                f"P1: {match.player1.name} : {match.score_player1} \n"
                f"P2: {match.player2.name} : {match.score_player2}  \n"
                f"Winner: {match.winner} \n"
            )

    def get_serialized(self):
        """Method returning serialized round"""
        serialized_round = {
            "name": self.name,
            "players_pair": self.players_pair,
            "matchs": self.matchs,
            "start_date": self.start_date,
            "end_date": self.end_date,
        }
        return serialized_round
