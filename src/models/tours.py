class Tours:
    """Class representing a round"""

    def __init__(self, matchs: list):
        """Constructor"""
        self.matchs = matchs

    def __str__(self):
        """Method returning round information"""
        return f"""
                Matchs : {self.matchs}
            """

    def __repr__(self):
        return str(self)
