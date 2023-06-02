from pydantic.dataclasses import dataclass
from typing import List
from collections import defaultdict
import dataclasses
from .round import Round
from .player import Player
import random

# flake8: noqa


@dataclass
class Tournament:
    """Class representing a tournament"""

    name: str
    location: str
    date_debut: str
    date_fin: str
    nb_rounds: int = 4
    rounds: List[tuple] = dataclasses.field(default_factory=list)
    players: List = dataclasses.field(default_factory=list)
    description: str = ""

    def create_round(self, round_number):
        """Method creating a round"""
        player_pairs = self.create_players_pairs(current_round=round_number)
        round = Round("Round " + str(round_number + 1), player_pairs)
        self.rounds.append(round)

    def create_players_pairs(self, current_round):
        """Method creating pairs of players"""
        players_pairs = []

        # --- First round ---
        if current_round == 0:
            # --- Shuffle players ---
            players = self.players.copy()
            random.shuffle(players)
        # --- Other rounds ---
        else:
            players = sorted(self.players, key=lambda x: x.ranking, reverse=False)

        # --- Create pairs ---
        # Split players list in two
        half_len = len(players) // 2
        sup_part = players[:half_len]
        inf_part = players[half_len:]

        # Create pairs
        # if players have already played together, switch the second player
        # in played_with compared with the first_name and name
        # and if players have the same score, switch the second player
        # at the end add first_name and name to played_with
        for i in range(half_len):
            if inf_part[i].first_name + inf_part[i].name in sup_part[i].played_with:
                if inf_part[i].ranking == sup_part[i].ranking:
                    players_pairs.append([sup_part[i], inf_part[i + 1]])
                    sup_part[i].played_with.append(
                        f"{inf_part[i + 1].first_name} {inf_part[i + 1].name}"
                    )
                    inf_part[i + 1].played_with.append(
                        f"{sup_part[i].first_name} {sup_part[i].name}"
                    )
            else:
                players_pairs.append([sup_part[i], inf_part[i]])
                sup_part[i].played_with.append(
                    f"{inf_part[i].first_name} {inf_part[i].name}"
                )
                inf_part[i].played_with.append(
                    f"{sup_part[i].first_name} {sup_part[i].name}"
                )

        return players_pairs

    def get_ranking(self, by_score=False):
        """Method returning the ranking of the tournament"""
        if by_score:
            return sorted(self.players, key=lambda x: x.total_score, reverse=True)
        else:
            return sorted(self.players, key=lambda x: x.ranking, reverse=True)

    def get_serialized(self):
        """Method returning the serialized tournament"""
        serialized_tournament = {
            "name": self.name,
            "location": self.location,
            "date_debut": self.date_debut,
            "date_fin": self.date_fin,
            "nb_rounds": self.nb_rounds,
            "rounds": [round.get_serialized() for round in self.rounds],
            "players": [player.get_serialized() for player in self.players],
            "description": self.description,
        }

        return serialized_tournament
