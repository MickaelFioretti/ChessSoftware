class Tournois:
    """Class representing a tournament"""

    def __init__(
        self,
        name,
        location,
        date,
        tours,
        joueurs: list,
        time_control,
        description,
        number_of_rounds=4,
    ):
        """Constructor"""
        self.name = name
        self.location = location
        self.date = date
        self.number_of_rounds = number_of_rounds
        self.tours = tours
        self.joueurs = joueurs
        self.time_control = time_control
        self.description = description

    def add_player(self, player):
        """Method adding a player to the tournament"""
        self.joueurs.append(player)

    # def display_classements(self):
    #     """Method displaying the tournament rankings"""
    #     # Sort players by ranking and display them
    #     self.joueurs.sort(key=lambda x: x.ranking)
    #     for player in self.joueurs:
    #         player.display()

    def display(self):
        """Method displaying tournament information"""
        print(
            f"""
                Nom du tournoi : {self.name}\n
                Lieu : {self.location}\n
                Date : {self.date}\n
                Nombre de tours : {self.number_of_rounds}\n
                Liste des joueurs : {self.joueurs}\n
                Contrôle du temps : {self.time_control}\n
                Description : {self.description}
            """
        )
