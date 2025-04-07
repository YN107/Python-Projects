class Customer:
    def __init__(self, name, address, phone_num, email):
        self.name = name
        self.address = address
        self.phone_num = phone_num
        self.email = email
        self.accounts = {}

    def add_account(self,account):
        self.accounts[account.number] = account