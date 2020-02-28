import unittest

from Bdd import Bdd
from Compte import Compte


class MyTestCase(unittest.TestCase):
    def test_recuperer_compte_par_id_existant_renvoie_compte_avec_id_correspondant_et_solde_et_status_message_ok(self):
        # Given
        idCompte = 2

        # When
        result = Bdd.recuperer_compte_bdd(idCompte)

        # Then
        self.assertTrue(type(result) == dict)
        self.assertTrue('solde' in result)
        self.assertTrue('id_compte' in result)
        self.assertTrue('status' in result)
        self.assertEqual(idCompte, result['id_compte'])
        self.assertEqual('GET COMPTE OK', result['status'])

    def test_maj_compte_existant_ancien_solde_1000_nouveau_solde_2000_retour_MAJ_OK(self):
        # Given
        compteExistant = Compte(1, 2000)

        # When
        result = Bdd.majCompte(compteExistant)

        # Then
        self.assertTrue(type(result) == dict)
        self.assertTrue('status' in result)
        self.assertTrue('solde' in result)
        self.assertTrue('id_compte' in result)
        self.assertEqual('MAJ OK', result['status'])
        self.assertEqual(1, result['id_compte'])
        self.assertEqual(2000, result['solde'])

    def test_recuperer_compte_par_id_inexistant_renvoie_erreur_compte_inexistant(self):
        # Given
        idCompte = 200

        # When
        result = Bdd.recuperer_compte_bdd(idCompte)

        # Then
        self.assertTrue(type(result) == dict)
        self.assertEqual('ERREUR: COMPTE INEXISTANT', result['status'])

    def test_maj_compte_inexistant_renvoie_(self):
        # Given
        compteExistant = Compte(1, 2000)

        # When
        result = Bdd.majCompte(compteExistant)

        # Then
        self.assertTrue(type(result) == dict)
        self.assertTrue('status' in result)
        self.assertTrue('solde' in result)
        self.assertTrue('id_compte' in result)
        self.assertEqual('MAJ OK', result['status'])
        self.assertEqual(1, result['id_compte'])
        self.assertEqual(2000, result['solde'])


if __name__ == '__main__':
    unittest.main()
