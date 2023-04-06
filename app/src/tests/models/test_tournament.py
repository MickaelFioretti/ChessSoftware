import pytest

from models.tournament import Tournament, Player

@pytest.fixture
def tournament():
    # Fixture pour initialiser le tournoi avec 4 joueurs
    tournament = Tournament()
    players = [
        Player(first_name="Jean", name="Dupont", birth_date="20/03/2023"),
        Player(first_name="Fioretti", name="Mickael", birth_date="20/03/2023"),
        Player(first_name="Julien", name="Levieux", birth_date="20/02/2020"),
        Player(first_name="Tony", name="Stark", birth_date="20/02/2020")
    ]
    tournament.add_players(players)
    return tournament


def test_create_players_pairs(tournament):
    # Test pour vérifier que la fonction crée des paires correctes pour le premier tour
    pairs = tournament.create_players_pairs(current_round=0)
    assert len(pairs) == 2
    assert pairs[0][0].name == "Dupont"
    assert pairs[0][1].name == "Levieux"
    assert pairs[1][0].name == "Stark"
    assert pairs[1][1].name == "Mickael"