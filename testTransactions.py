import unittest

from Compte import Compte
from Transaction import Transaction


class MyTestCase(unittest.TestCase):

    def test_sauvegarde_instance_de_transaction_retour_ok(self):
        # Given
        transaction = Transaction(Compte(1,1000), 'depot',
        '25/02/2020', 500, 1500)

        # When


        # Then
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
