# --- imports ---
import json

# --- models ---
from models.player import Player
from models.tournament import Tournament
from models.match import Match
from models.round import Round

path_json = "/home/user/app/src/bdd/"


# --------- save data ---------
def save_data(key, data):
    with open(f"{path_json}db.json", "r") as json_file:
        data_db = json.load(json_file)

    # --- if key already exists ---
    if key in data_db:
        # --- add data to db ---
        data_db[key].append(data)
    else:
        data_db[key] = [data]
    with open(f"{path_json}db.json", "w") as json_file:
        json.dump(data_db, json_file, indent=4)


# --------- update data ---------
def update_data(data_type: str, identifier: str, new_data: dict):
    with open(f"{path_json}db.json", "r") as json_file:
        data_db = json.load(json_file)

    # --- update data ---
    for data in data_db[data_type]:
        if data["name"] == identifier:
            for key, value in new_data.items():
                data[key] = value

    # --- save data ---
    with open(f"{path_json}db.json", "w") as json_file:
        json.dump(data_db, json_file, default=lambda o: o.get_serialized(), indent=4)


# --------- load data ---------
def load_data():
    try:
        with open(f"{path_json}db.json", "r") as json_file:
            if json_file.read().strip() == "":
                return {}
            json_file.seek(0)
            data = json.load(json_file)
    except FileNotFoundError:
        data = {}
    return data


def load_player(serialized_player, load_tournament_score=False):
    player = Player(
        serialized_player["first_name"],
        serialized_player["name"],
        serialized_player["birth_date"],
        serialized_player["total_score"],
        serialized_player["ranking"],
    )

    if load_tournament_score:
        player.tournament_score = serialized_player["tournament_score"]
    return player


def load_tournament(serialized_tournament):
    loaded_tournament = Tournament(
        serialized_tournament["name"],
        serialized_tournament["location"],
        serialized_tournament["date_debut"],
        serialized_tournament["date_fin"],
        serialized_tournament["nb_rounds"],
        [],
        [
            load_player(player, load_tournament_score=True)
            for player in serialized_tournament["players"]
        ],
        serialized_tournament["description"],
    )

    loaded_tournament.rounds = load_rounds(serialized_tournament, loaded_tournament)

    return loaded_tournament


def load_rounds(serialized_tournament, tournament):
    loaded_rounds = []

    # --- ---
    for round in serialized_tournament["rounds"]:
        players_pair = []
        for pair in round["players_pair"]:
            for player in tournament.players:
                if player.name == pair[0]["name"]:
                    player1 = player
                if player.name == pair[1]["name"]:
                    player2 = player
            players_pair.append([player1, player2])
        loaded_round = Round(round["name"], players_pair, load_match=True)
        loaded_round.matchs = [
            load_match(match, tournament) for match in round["matchs"]
        ]
        loaded_round.start_date = round["start_date"]
        loaded_round.end_date = round["end_date"]
        loaded_rounds.append(loaded_round)

    return loaded_rounds


def load_match(serialized_match, tournament):
    player1 = None
    player2 = None

    for player in tournament.players:
        print("Top of the IF : ", player.name)
        if player.name == serialized_match["player1"]["name"]:
            print(player.name, " ===J1=== ", serialized_match["player1"]["name"])
            player1 = player
        elif player.name == serialized_match["player2"]["name"]:
            print(player.name, " ===J2=== ", serialized_match["player2"]["name"])
            player2 = player

    loaded_match = Match(
        player1=player1,
        player2=player2,
        name=serialized_match["name"],
    )
    loaded_match.score_player1 = serialized_match["score_player1"]
    loaded_match.score_player2 = serialized_match["score_player2"]
    loaded_match.winner = serialized_match["winner"]

    return loaded_match
