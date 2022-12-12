class Matchs:
    """Class Matchs"""

    def __init__(self, joueur1, joueur2, joueur1_score, joueur2_score):
        """Constructor"""
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.joueur1_score = joueur1_score
        self.joueur2_score = joueur2_score

    def __str__(self):
        """Method returning match information"""
        return f"""
                Joueur 1 : {self.joueur1}\n
                Joueur 2 : {self.joueur2}\n
                Score Joueur 1 : {self.joueur1_score}\n
                Score Joueur 2 : {self.joueur2_score}
            """

    def __repr__(self):
        return str(self)
