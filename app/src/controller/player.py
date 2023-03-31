# --- imports ---

# --- controllers ---
from controller.database import update_data

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
        user_entries["name"],
        user_entries["first_name"],
        user_entries["birth_date"],
        user_entries["total_score"],
        user_entries["ranking"],
    )

    return player


def update_ranking(player, ranking, score=True):
    if score:
        player.total_score += player.tournament_score
    player.ranking = ranking
    update_data("players", player.name, player.get_serialized())
    print(f"Le joueur {player.first_name} {player.name} a bien été mis à jour")
