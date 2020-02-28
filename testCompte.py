import unittest
from Compte import *
from unittest.mock import patch

class MyTestCase(unittest.TestCase):

    @patch('Compte.Bdd.recuperer_compte_bdd')
    def test_si_recuperation_compte_existant_par_id_alors_compte_recupere_contient_id_et_solde(self, stubBdd):
        # Given
        idCompte = 1
        solde = 1000

        stubBdd.return_value = {'id_compte': 1, 'solde': 1000}

        # When
        resultCompte = Compte.recuperer_compte(idCompte)

        # Then
        self.assertTrue(type(resultCompte) == Compte)
        self.assertEqual(idCompte, resultCompte._idCompte)
        self.assertEqual(solde, resultCompte._solde)



if __name__ == '__main__':
    unittest.main()
