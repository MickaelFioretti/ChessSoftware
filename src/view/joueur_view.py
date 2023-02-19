# --- Classe JoueurView ---
class JoueurView:
    def display(self, joueurs):
        print("Liste des joueurs:")
        for joueur in joueurs:
            print(f"{joueur.first_name} {joueur.last_name} {joueur.ranking} ")
