# --- imports ---
import json
import uuid

path_json = "/workspaces/ChessSoftware/src/bdd/"


# --- json database ---
def load_data(key):
    with open(f"{path_json}db.json", "r") as json_file:
        data = json.load(json_file)
    return data


def save_data(key, data):
    with open(f"{path_json}db.json", "r") as json_file:
        data_db = json.load(json_file)

    # --- if key already exists ---
    if key in data_db:
        # --- generate id ---
        player_id = str(uuid.uuid4())

        # --- add id to data ---
        data["id"] = player_id

        # --- add data to db ---
        data_db[key].append(data)
    else:
        data_db[key] = [data]

    with open(f"{path_json}db.json", "w") as json_file:
        json.dump(data_db, json_file, indent=4)
