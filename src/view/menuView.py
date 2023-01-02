from pydantic.dataclasses import dataclass
from typing import List
import os


@dataclass
class MenuOption:
    name: str
    value: str


@dataclass
class MenuView:
    """Class to display a menu and handle user input"""

    title: str
    options: List[MenuOption]

    def display(self):
        """Display the menu"""
        os.system("cls" if os.name == "nt" else "clear")
        print(self.title)
        print()
        for i, option in enumerate(self.options):
            print(f"{i + 1} - {option.name}")
        print()
        choice = input("Choisissez une option: ")
        return int(choice)
