from view.base import BaseView


class CreatePlayer(BaseView):
    def display_menu(self):
        last_name = input("Entrez le nom du joueur: ")
        first_name = input("Entrez le prénom du joueur: ")
        birth_date = self.get_user_input(
            msg_display="Entrez la date de naissance du joueur (jj/mm/aaaa): ",
            msg_error="Veuillez entrer une date valide",
            value_type="date",
        )
        ranking = self.get_user_input(
            msg_display="Entrez le classement du joueur (0 a 1000): ",
            msg_error="Veuillez entrer un classement valide",
            value_type="numeric",
        )

        print(f"Le joueur {first_name} {last_name} a bien été créé")

        return {
            "last_name": last_name,
            "first_name": first_name,
            "birth_date": birth_date,
            "total_score": 0,
            "ranking": ranking,
        }
