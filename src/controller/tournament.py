# --- import ---
import os

# --- Models ---
from models.tournament import Tournament

# --- Views ---
from view.base_view import BaseView
from view.tournament import CreateTournament, LoadTournament
from view.player import LoadPlayer

# --- Controllers ---
from controller.player import create_player, update_ranking
from controller.database import save_data, load_player, load_tournament


def create_tournament():
    menu = BaseView()

    # Recuperation des donnees du tournoi
    user_entry = CreateTournament().display_menu()

    # Chargement des joueurs
    os.system("clear")
    user_input = menu.get_user_input(
        msg_display="Que voulez-vous faire ?\n1 - Charger des joueurs existants\n2 - Créer des joueurs\n",
        msg_error="Veuillez entrer un nombre valide",
        value_type="selection",
        assertions=["1", "2"],
    )

    # Chargement des joueurs existants
    if user_input == "1":
        players = []
        user_input = menu.get_user_input(
            msg_display="Combien de joueurs voulez-vous charger ?\n",
            msg_error="Veuillez entrer un nombre valide",
            value_type="numeric",
        )
        serialized_players = LoadPlayer().display_menu(
            nb_players_to_load=int(user_input)
        )
        for serialized_player in serialized_players:
            player = load_player(serialized_player)
            players.append(player)

    # Creation de joueurs
    else:
        print(f"Creation de {str(user_entry['nb_players'])} joueurs")
        players = []
        while len(players) < int(user_entry["nb_players"]):
            players.append(create_player())

    # Creation du tournoi
    tournament = Tournament(
        user_entry["name"],
        user_entry["location"],
        user_entry["date_debut"],
        user_entry["date_fin"],
        user_entry["nb_rounds"],
        [],
        players,
        user_entry["description"],
    )

    # --- Sauvegarde du tournoi ---
    save_data("tournaments", tournament.get_serializeed_tournament())

    return tournament


def play_tournament(tournament, new_tournament_loaded=False):
    menu = BaseView()
    print()
    print(f"Début du tournoi {tournament.name} le {tournament.date_debut}")
    print()

    while True:
        # Si nouveau tournois charge: calcul des rounds restants
        a = 0
        if new_tournament_loaded:
            for round in tournament.rounds:
                if round.end_date == "":
                    a += 1
            nb_rounds_to_play = tournament.nb_rounds - a
            new_tournament_loaded = False
        else:
            nb_rounds_to_play = tournament.nb_rounds

        for i in range(nb_rounds_to_play):
            # Creation du round
            tournament.create_round(round_number=i + a)

            # On joue le dernier round cree
            current_round = tournament.rounds[-1]
            print()
            print(current_round.start_date + " : Début du round " + current_round.name)

            # Round terminé, on passe au round suivant, on peux aussi mettre a jour le classement
            while True:
                print()
                user_input = menu.get_user_input(
                    msg_display="Que faire ?\n"
                    "1 - Round suivant\n"
                    "2 - Voir le classement\n"
                    "3 - Mettre à jour le classement\n"
                    "4 - Sauvegarder le tournoi\n"
                    "5 - Charger un tournoi\n",
                    msg_error="Veuillez entrer un nombre valide",
                    value_type="selection",
                    assertions=["1", "2", "3", "4", "5"],
                )
                print()

                # Round suivant
                if user_input == "1":
                    current_round.mark_as_completed()
                    break

                # Voir le classement
                elif user_input == "2":
                    print(f"Classement du tournoi {tournament.name}")
                    for i, player in enumerate(tournament.get_ranking()):
                        print(f"{i + 1} - {player.name} ({player.score})")

                # Mettre à jour le classement
                elif user_input == "3":
                    for player in tournament.players:
                        rank = menu.get_user_input(
                            msg_display=f"Rang de {player.name} :\n",
                            msg_error="Veuillez entrer un nombre valide",
                            value_type="numeric",
                        )
                        update_ranking(player, rank, score=False)

                # Sauvegarder le tournoi
                elif user_input == "4":
                    rankings = tournament.get_ranking()
                    for i, player in enumerate(rankings):
                        for player2 in enumerate(tournament.players):
                            if player.name == player2.name:
                                player2.rank = i + 1
                    # TODO : save tournament in database

                # Charger un tournoi
                elif user_input == "5":
                    serialized_loaded_tournament = LoadTournament().display_menu()
                    tournament = load_tournament(serialized_loaded_tournament)
                    new_tournament_loaded = True
                    break

            if new_tournament_loaded:
                break

        if new_tournament_loaded:
            continue

        else:
            break

    # Une fois le tournois terminé, on affiche le classement final
    rankings = tournament.get_ranking()
    for i, player in enumerate(rankings):
        for player2 in tournament.players:
            if player.name == player2.name:
                player2.total_score += player.tournament_score
                player2.rank = i + 1
    # TODO : update player in database
    return rankings
