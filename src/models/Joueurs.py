class Joueurs:
    """Classe représentant un joueur de d'échecs"""

    def __init__(self, first_name, last_name, birth_date, sexe, ranking):
        """Constructeur de notre classe"""
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.sexe = sexe
        self.ranking = ranking

    def __str__(self):
        """Méthode affichant les informations d'un joueur"""
        return f"""
                Nom : {self.last_name}\n
                Prénom : {self.first_name}\n
                Date de naissance : {self.birth_date}\n
                Sexe : {self.sexe}\n
                Ranking : {self.ranking}
            """

    def __repr__(self):
        return str(self)

    def display(self):
        """Méthode affichant les informations d'un joueur"""
        print(
            f"""
                Nom : {self.last_name}\n
                Prénom : {self.first_name}\n
                Date de naissance : {self.birth_date}\n
                Sexe : {self.sexe}\n
                Ranking : {self.ranking}
            """
        )
