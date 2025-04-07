class Authenticator:
    def __init__(self,bank):
        self.bank = bank

    def authenticate(self,number,pin):
        for account in self.bank.accounts.values():
            if account.card and account.card.number == number and account.card.get_PIN() == pin:
                return account
        return None