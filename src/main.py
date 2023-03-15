# from controller.tournament_controller import TournamentController

# --- View ---
from view.menu_view import MainMenu


def main():
    MainMenu().display_main_menu()

    # # Create an instance of the menu controller and pass the view
    # controller = TournamentController()

    # # Run the controller
    # controller.run()


if __name__ == "__main__":
    main()
