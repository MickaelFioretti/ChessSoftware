# --- PIP ---
from pydantic.dataclasses import dataclass
from typing import List

# --- LOCAL ---
from utils.clear_shell import clear_shell


@dataclass
class MenuOption:
    """Class to represent a menu option"""

    name: str
    value: str


@dataclass
class MenuView:
    """Class to display a menu and handle user input"""

    title: str
    options: List[MenuOption]

    def display(self):
        """Display the menu"""
        clear_shell()
        print(self.title)
        print()
        for i, option in enumerate(self.options):
            print(f"{i + 1} - {option.name}")
        print()
        choice = input("Choisissez une option: ")
        return int(choice)
