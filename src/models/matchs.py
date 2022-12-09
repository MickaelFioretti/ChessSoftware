class Matchs:
    """Class Matchs"""

    def __init__(self, joueur1, joueur2, joueur1_score, joueur2_score):
        """Constructor"""
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.joueur1_score = joueur1_score
        self.joueur2_score = joueur2_score

    def display(self):
        """Method displaying match information"""
        print("Joueur 1 : {}".format(self.joueur1))
        print("Joueur 2 : {}".format(self.joueur2))
        print("Score Joueur 1 : {}".format(self.joueur1_score))
        print("Score Joueur 2 : {}".format(self.joueur2_score))
