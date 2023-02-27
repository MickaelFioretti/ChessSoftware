from pydantic.dataclasses import dataclass
from typing import List

from .round import Round
from .player import Player


@dataclass
class Tournament:
    """Class representing a tournament"""

    name: str
    location: str
    date_debut: str
    date_fin: str
    nombre_de_tours: int = 4
    nb_rounds: int = 1
    rounds: List[Round] = List[Round]
    players: List[players] = List[Player]
    description: str = ""

    def add_player(self, player):
        """Method adding a player to the tournament"""
        self.players.append(player)

    def add_tour(self, tour: Round):
        """Method adding a round to the tournament"""
        self.rounds.append(tour)

    def create_round(self, round_number):
        """Method creating a round"""
        player_pairs = self.create_players_pairs(current_round=round_number)
        round = Round("Round " + str(round_number + 1), player_pairs)
        self.rounds.append(round)

    def create_players_pairs(self, current_round):
        """Method creating pairs of players"""

        # --- First round sort player by rank ---
        if current_round == 0:
            sorted_players = sorted(self.players, key=lambda x: x.ranking, reverse=True)

        # --- Other rounds sort player by score ---
        else:
            sorted_players = []
            score_sorted_players = sorted(
                self.players, key=lambda x: x.total_score, reverse=True
            )

            # --- Sort by rank if same score ---
            # TODO: Refaire cette partie
            for i, player in enumerate(score_sorted_players):
                try:
                    sorted_players.append(player)
                except player.total_score == score_sorted_players[i + 1].total_score:
                    if player.ranking < score_sorted_players[i + 1].rank:
                        hi_player = player
                        lo_player = score_sorted_players[i + 1]
                    else:
                        hi_player = score_sorted_players[i + 1]
                        lo_player = player
                    sorted_players.append(hi_player)
                    sorted_players.append(lo_player)
                except IndexError:
                    sorted_players.append(player)

            # --- Split players in two parts ---
            # flake8: noqa
            # TODO: Refaire cette partie
            sup_part = sorted_players[len(sorted_players) // 2 :]
            inf_part = sorted_players[: len(sorted_players) // 2]

            players_pairs = []

            # --- Create pairs ---
            for i, player in enumerate(sup_part):
                a = 0
                while True:
                    try:
                        player2 = inf_part[i + a]

                    #  --- Add player1 at the last player of the inf list ---
                    except IndexError:
                        player2 = inf_part[i]
                        players_pairs.append([player, player2])

                        # --- Add the player to the list played_with ---
                        player.played_with.append(player2)
                        player2.played_with.append(player)
                        break

                    # --- if player 1 as played with player 2 try with the next player ---
                    if player in player2.played_with:
                        a += 1
                        continue

                    # If the 2 players have never played together, we create the peer, then
                    # We assign players in their respective Played_with list
                    # to indicate that they have already played together
                    else:
                        players_pairs.append([player, player2])
                        player.played_with.append(player2)
                        player2.played_with.append(player)
                        break

        return players_pairs

    def get_ranking(self):
        """Method getting the ranking of the tournament"""
        return sorted(self.players, key=lambda x: x.total_score, reverse=True)
