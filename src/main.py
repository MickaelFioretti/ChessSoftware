from controller.tournament_controller import TournamentController


def main():

    # Create an instance of the menu controller and pass the view
    controller = TournamentController()

    # Run the controller
    controller.run()


if __name__ == "__main__":
    main()
