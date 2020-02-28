import data as data


class Bdd:

    def __init__(self):
        pass

    @staticmethod
    def recuperer_compte_bdd(id):
        if id in data.comptes:
            result = data.comptes[id]
            result['status'] = 'GET COMPTE OK'
        else:
            result = {'status': 'ERREUR: COMPTE INEXISTANT'}
        return result


    @staticmethod
    def majCompte(compte):
        # MAJ
        data.comptes[compte._idCompte] = {'id_compte': compte._idCompte,
                                   'solde' : compte._solde}

        # Get compte
        result = Bdd.recuperer_compte_bdd(compte._idCompte)

        return {'status' : 'MAJ OK', 'solde': result['solde'],
                'id_compte': result['id_compte'],
                }