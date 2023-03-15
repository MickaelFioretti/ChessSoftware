# --- imports ---
from pydantic.dataclasses import dataclass
import dataclasses
from typing import List, Tuple

# --- models ---
from models.match import Match

# --- controller ---
from controller.timestamp import get_timestamp


@dataclass
class Round:
    """Class representing a round"""

    name: str
    players_pair: List[Tuple[str, str]] = dataclasses.field(default_factory=list)
    matchs: List[Tuple[str, str]] = dataclasses.field(default_factory=list)
    start_date: str = get_timestamp()
    end_date: str = ""
    load_matchs: bool = False

    def __post_init__(self):
        if self.load_matchs:
            self.matchs = []
        else:
            self.matchs = self.create_matchs()

    def create_matchs(self):
        """Method creating matchs"""
        matchs = []
        for i, pair in enumerate(self.players_paits):
            matchs.append(Match(name=f"Match {i}", players_pair=pair))
        return matchs

    def play_round(self):
        self.end_date = get_timestamp()
        for match in self.matchs:
            match.play_match()
