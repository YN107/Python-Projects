class Bank:
    def __init__(self, name, swift_code):
        self.name = name
        self.swift_code = swift_code
        self.accounts = {}

    def add_customer(self, customer):
        for account in customer.accounts.values():
            self.accounts[account.number] = account