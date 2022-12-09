class Tours:
    """Class representing a round"""

    def __init__(self, matchs: list):
        """Constructor"""
        self.matchs = matchs

    def display(self):
        """Method displaying round information"""
        print("Matchs : {}".format(self.matchs))
