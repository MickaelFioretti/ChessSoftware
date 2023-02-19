from .joueur import (
    Joueur,
    SexeError,
    RankingError,
    MINIMAL_RANKING_VALUE,
    MAXIMAL_RANKING_VALUE,
)
import pytest

NORMAL_PLAYER = Joueur("Dupont", "Jean", "01/01/1900", "M", 1)


def test_init_Joueur() -> None:
    """Test the constructor of the class Joueur"""
    assert NORMAL_PLAYER.first_name == "Dupont"
    assert NORMAL_PLAYER.last_name == "Jean"
    assert NORMAL_PLAYER.birth_date == "01/01/1900"
    assert NORMAL_PLAYER.genre == "M"
    assert NORMAL_PLAYER.ranking == 1


def test_Joueur_sexe_initialisation_sexe_error() -> None:
    with pytest.raises(SexeError):
        Joueur("Dupont", "Jean", "01/01/1900", "P", 1)


def test_Joueur_sexe_initialisation_ranking_error() -> None:
    with pytest.raises(RankingError):
        Joueur("Dupont", "Jean", "01/01/1900", "M", MINIMAL_RANKING_VALUE - 1)
        Joueur("Dupont", "Jean", "01/01/1900", "M", MAXIMAL_RANKING_VALUE + 1)


def test_Joueur_win_standard_case() -> None:
    """Test the method win of the class Joueur"""
    NORMAL_PLAYER.win()
    assert NORMAL_PLAYER.ranking == 2
