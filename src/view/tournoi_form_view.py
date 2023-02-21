class TournoiFormView:
    def display(self):
        print("Ajouter un tournoi")
        print("Entrez les infomations suivantes:")
        name = input("Nom: ")
        location = input("Lieu: ")
        date_debut = input("Date de début (jj/mm/aaaa): ")
        date_fin = input("Date de fin (jj/mm/aaaa): ")
        nombre_de_tours = input("Nombre de tours: ")
        numero_tour_actuel = input("Numero du tour actuel: ")
        description = input("Description: ")
        return {
            "name": name,
            "location": location,
            "date_debut": date_debut,
            "date_fin": date_fin,
            "nombre_de_tours": nombre_de_tours,
            "numero_tour_actuel": numero_tour_actuel,
            "description": description,
        }
