from pydantic.dataclasses import dataclass
from typing import List


@dataclass
class MenuOption:
    name: str
    value: str


@dataclass
class MenuView:
    """Class to display a menu and handle user input"""

    title: str
    options: List[MenuOption]

    def display_menu(self):
        print("Menu")
        for option in self.options:
            print(f"{option.name} - {option.value}")

    def get_menu_choice(self):
        choice = input("Enter your choice: ")
        return choice

    def run(self):
        while True:
            self.display_menu()
            choice = self.get_menu_choice()
            option = next(
                (option for option in self.options if option.value == choice), None
            )
            if option:
                self.handle_option(option)
            else:
                print(f"Invalid choice: {choice}")

    def handle_option(self, option: MenuOption):
        if option.name == self.options[0].name:
            print(f'You selected "{option.name}"')
            # TODO: Add code to handle this option
        elif option.name == self.options[1].name:
            print(f'You selected "{option.name}"')
            # TODO: Add code to handle this option
        elif option.name == self.options[2].name:
            print(f'You selected "{option.name}"')
            # TODO: Add code to handle this option
        elif option.name == "Exit":
            print("Exiting")
            exit()
        else:
            print(f"Invalid option: {option.name}")
