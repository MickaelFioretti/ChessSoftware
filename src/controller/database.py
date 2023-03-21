# --- imports ---
import json
import uuid

# --- models ---
from models.player import Player

path_json = "/workspaces/ChessSoftware/src/bdd/"


# ------ load data ------


# --- load all data ---
def load_data(key):
    with open(f"{path_json}db.json", "r") as json_file:
        data = json.load(json_file)
    return data


# --- load player data ---
def load_player(serialized_player, load_tournament_score=False):
    player = Player(
        serialized_player["first_name"],
        serialized_player["last_name"],
        serialized_player["birth_date"],
        serialized_player["total_score"],
        serialized_player["ranking"],
    )
    player.id = serialized_player["id"]

    if load_tournament_score:
        player.tournament_score = serialized_player["tournament_score"]
    return player


def save_data(key, data):
    with open(f"{path_json}db.json", "r") as json_file:
        data_db = json.load(json_file)

    # --- if key already exists ---
    if key in data_db:
        # --- generate id ---
        id = str(uuid.uuid4())

        # --- add id to data ---
        data["id"] = id

        # --- add data to db ---
        data_db[key].append(data)
    else:
        data_db[key] = [data]

    with open(f"{path_json}db.json", "w") as json_file:
        json.dump(data_db, json_file, indent=4)
