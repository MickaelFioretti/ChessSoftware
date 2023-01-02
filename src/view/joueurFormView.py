class JoueurFormView:
    def display(self):
        print("Ajouter un joueur")
        print("Entrez les infomations suivantes:")
        first_name = input("Prénom: ")
        last_name = input("Nom: ")
        birth_date = input("Date de naissance (jj/mm/aaaa): ")
        sexe = input("Sexe (M/F): ")
        ranking = input("Classement: (0 a 1000) :")
        return {
            "first_name": first_name,
            "last_name": last_name,
            "birth_date": birth_date,
            "sexe": sexe,
            "ranking": ranking,
        }
