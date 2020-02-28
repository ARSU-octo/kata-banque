from Bdd import Bdd

class Compte:

    def __init__(self, idCompte, solde):
        self._idCompte = idCompte
        self._solde = solde
        pass

    @staticmethod
    def recuperer_compte(id):
        compte_bd = Bdd.recuperer_compte_bdd(id)

        # Transforme résultat BD en compte
        # ...

        return Compte(compte_bd['id_compte'], compte_bd['solde'])