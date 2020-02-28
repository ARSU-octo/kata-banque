import unittest
from Compte import *
from unittest.mock import patch


class MyTestCase(unittest.TestCase):
    @patch('Compte.Bdd.recuperer_compte_bdd')
    def test_si_recuperation_compte_existant_par_id_alors_compte_recupere_contient_id_et_solde(self, stubBdd):
        # Given
        idCompte = 1
        solde = 1000

        stubBdd.return_value = {'id_compte': 1, 'solde': 1000,
                                'status': 'GET COMPTE OK'}

        # When
        resultCompte = Compte.recuperer_compte(idCompte)

        # Then
        self.assertTrue(type(resultCompte) == Compte)
        self.assertEqual(idCompte, resultCompte._idCompte)
        self.assertEqual(solde, resultCompte._solde)

    @patch('Compte.Bdd.recuperer_compte_bdd')
    def test_si_recuperation_compte_inexistant_par_id_alors_retourne_compte_inexistant(self, stubBdd):
        # Given
        idCompte = 200

        stubBdd.return_value = {'status': "ERREUR: COMPTE INEXISTANT"}

        # When
        result = Compte.recuperer_compte(idCompte)

        # Then
        self.assertTrue(type(result) == dict)
        self.assertTrue('status' in result)
        self.assertEqual('ERREUR: COMPTE INEXISTANT', result['status'])

    @patch('Compte.Bdd.majCompte')
    def test_maj_compte_existant_par_id_1_et_solde_2000_alors_message_succes(self, stubBdd):
        # Given
        monCompte = Compte(1, 2000)
        nouv_solde = 2000

        stubBdd.return_value = {'status' : 'MAJ OK', 'solde': 1000,
                'id_compte': 1 }

        # When
        result = monCompte.maj_solde(nouv_solde)

        # Then
        self.assertTrue(type(result) == dict)
        self.assertTrue('status' in result)
        self.assertEqual('MAJ OK', result['status'])


if __name__ == '__main__':
    unittest.main()
