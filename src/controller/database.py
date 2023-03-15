# --- imports ---
import json

path_json = "/workspaces/ChessSoftware/src/bdd/"


# --- json database ---
def load_data(file_name):
    with open(f"{path_json}{file_name}.json", "r") as json_file:
        data = json.load(json_file)
    return data


def save_data(file_name, data):
    with open(f"{path_json}{file_name}.json", "w") as f:
        json.dump(data, f, indent=4)
