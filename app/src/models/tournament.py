from pydantic.dataclasses import dataclass
from typing import List
from collections import defaultdict
import dataclasses
from .round import Round
from .player import Player

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

        # --- First round sort player by rank ---
        if current_round == 0:
            sorted_players = sorted(self.players, key=lambda x: x.ranking, reverse=True)

        # --- Next rounds sort player by score ---
        else:
            sorted_players = []
            score_sorted_players = sorted(
                self.players, key=lambda x: x.total_score, reverse=True
            )

            # --- Sort by rank if same score ---
            for i in range(len(score_sorted_players)):
                player = score_sorted_players[i]
                sorted_players.append(player)
                if (
                    i < len(score_sorted_players) - 1
                    and player.total_score == score_sorted_players[i + 1].total_score
                ):
                    if player.ranking < score_sorted_players[i + 1].ranking:
                        hi_player = player
                        lo_player = score_sorted_players[i + 1]
                    else:
                        hi_player = score_sorted_players[i + 1]
                        lo_player = player
                    sorted_players.append(hi_player)
                    sorted_players.append(lo_player)

        # --- Create pairs ---
        # Split players in two parts
        half_len = len(sorted_players) // 2
        sup_part = sorted_players[half_len:]
        inf_part = sorted_players[:half_len]

        # Create pairs
        for i, player in enumerate(sup_part):
            for player2 in inf_part:
                if player2 not in player.played_with:
                    players_pairs.append([player, player2])
                    player.played_with.append(player2)
                    player2.played_with.append(player)
                    break
            else:
                players_pairs.append([player, inf_part[i % half_len]])
                player.played_with.append(inf_part[i % half_len])
                inf_part[i % half_len].played_with.append(player)
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
