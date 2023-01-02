from pydantic.dataclasses import dataclass


@dataclass
class Tours:
    """Class representing a round"""

    matchs: list
