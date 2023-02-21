from .base import BaseView


class JoueurFormView(BaseView):
    def display(self) -> dict:
        self.clear_shell()
        print("Ajouter un joueur")
        print("Entrez les infomations suivantes:")
        first_name = input("Prénom: ")
        last_name = input("Nom: ")
        birth_date = input("Date de naissance (jj/mm/aaaa): ")
        ranking = input("Classement: (0 a 1000) :")
        return {
            "first_name": first_name,
            "last_name": last_name,
            "birth_date": birth_date,
            "ranking": ranking,
        }
