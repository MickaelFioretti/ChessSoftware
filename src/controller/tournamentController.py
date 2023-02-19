from view.menuView import MenuView, MenuOption


class TournamentController:
    def __init__(self, view):
        self.view = view

    def run(self):
        self.view.run()


# Define the title and options for the menu
title = "Menu"
options = [
    MenuOption(name="Ajouter des joueur", value=1),
    MenuOption(name="Lister les joueur", value=2),
    MenuOption(name="Créer un tournois", value=3),
    MenuOption(name="Exit", value=4),
]

# Create an instance of the view
view = MenuView(title=title, options=options)

# Create an instance of the controller and pass the view to it
controller = TournamentController(view)

# Run the controller
controller.run()
