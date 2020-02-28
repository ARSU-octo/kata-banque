class Transaction:

    def __init__(self, compte, type, date, montant, balance=None):
        # self._idTransaction = None
        self._compte = compte
        self._type = type
        self._date = date
        self._balance = balance
        self._montant = montant
        pass

    @staticmethod
    def sauvegarder_en_Bdd(transaction):
        pass