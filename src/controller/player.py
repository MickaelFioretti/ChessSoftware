# --- imports ---

# --- models ---
from models.player import Player

# --- views ---
from view.player import CreatePlayer


# --- controllers ---
def create_player():
    # Recuperation des infos du joueur
    user_entries = CreatePlayer().display_menu()

    # Creation du joueur
    player = Player(
        user_entries["last_name"],
        user_entries["first_name"],
        user_entries["birth_date"],
        user_entries["total_score"],
        user_entries["ranking"],
    )

    # TODO: save player

    return player


def update_ranking(player, ranking, score=True):
    if score:
        player.total_score += player.tournament_score
    player.ranking = ranking
    # update_player_ranking("player", player)
    print(f"Le joueur {player.first_name} {player.last_name} a bien été mis à jour")
