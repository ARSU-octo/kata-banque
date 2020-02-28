from Bdd import Bdd

class Compte:

    def __init__(self, idCompte, solde):
        self._idCompte = idCompte
        self._solde = solde
        pass


    def maj_solde(self, nouveauSolde):
        self._solde = nouveauSolde
        result = Bdd.majCompte(self)
        return result


    @staticmethod
    def recuperer_compte(id):
        compte_bd = Bdd.recuperer_compte_bdd(id)

        # Transforme résultat BD en compte
        # ...
        if compte_bd['status'] == 'GET COMPTE OK':
            return Compte(compte_bd['id_compte'], compte_bd['solde'])
        else:
            return compte_bd