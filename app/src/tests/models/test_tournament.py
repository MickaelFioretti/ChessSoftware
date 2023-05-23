import pytest

from models.tournament import Tournament
from models.player import Player


@pytest.fixture
def tournament():
    # Fixture pour initialiser le tournoi avec 4 joueurs
    tournament = Tournament(
        name="Tournoi test",
        location="Paris",
        date_debut="01/01/2021",
        date_fin="01/01/2021",
        nb_rounds=4,
        players=[
            Player(
                first_name="Mickael",
                name="Stark",
                birth_date="01/01/1980",
                ranking=1,
                played_with=[],
            ),
            Player(
                first_name="Jean",
                name="Dupont",
                birth_date="01/01/1980",
                ranking=3,
                played_with=[],
            ),
            Player(
                first_name="Paul",
                name="Levieux",
                birth_date="01/01/1980",
                ranking=4,
                played_with=[],
            ),
            Player(
                first_name="Jacques",
                name="Lefou",
                birth_date="01/01/1980",
                ranking=2,
                played_with=[],
            ),
        ]
    )

    return tournament


def test_create_players_pairs(tournament):
    """Test pour vérifier que la fonction crée des paires
    correctes pour le premier tour"""

    pairs = tournament.create_players_pairs(current_round=1)

    # Test que les paire sont bien créées et que
    # chaque joueur ne joue qu'une fois
    assert len(pairs) == 2
    assert len(pairs[0]) == 2
    assert len(pairs[1]) == 2
    assert pairs[0][0] != pairs[0][1]
    assert pairs[1][0] != pairs[1][1]
    assert pairs[0][0] != pairs[1][0]
    assert pairs[0][0] != pairs[1][1]
    assert pairs[0][1] != pairs[1][0]
    assert pairs[0][1] != pairs[1][1]
    
    # Test que les paires sont bien créées en fonction du classement
    assert pairs[0][0].ranking < pairs[0][1].ranking
    assert pairs[1][0].ranking < pairs[1][1].ranking
    
    # Test que le played_with est bien mis à jour
    assert pairs[0][0].played_with == [f"{pairs[0][1].first_name} {pairs[0][1].name}"]
    assert pairs[0][1].played_with == [f"{pairs[0][0].first_name} {pairs[0][0].name}"]
    assert pairs[1][0].played_with == [f"{pairs[1][1].first_name} {pairs[1][1].name}"]
    assert pairs[1][1].played_with == [f"{pairs[1][0].first_name} {pairs[1][0].name}"]
