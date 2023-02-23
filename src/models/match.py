from pydantic.dataclasses import dataclass


@dataclass
class Match:
    """Class Matchs"""

    joueur1: str
    joueur2: str
    result: str = None

    def update_result(self, result):
        """Update the result of the match"""
        self.result = result
        if result == "win":
            self.joueur1.add_points(1)
        elif result == "loose":
            self.joueur2.add_points(1)
        elif result == "draw":
            self.joueur1.add_points(0.5)
            self.joueur2.add_points(0.5)
