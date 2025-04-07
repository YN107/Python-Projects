from screen import Screen
class Account:
    def __init__(self, number):
        self.number = number
        self.balance = 0
        self.card = None
        self.transactions_history = []
    def __str__(self):
        return f"Account Number: {self.number},\nBalance: {self.balance},\nLinked Card: ({self.card})\n,Transactions History: {self.transactions_history}\n"
    def add_trs(self, trs):
        self.transactions_history.append(trs)
    def add_card(self,card):
        self.card = card
    def display_transactions_history(self):
        if not self.transactions_history:
            Screen().line(8)
            print("No transactions available")
            return
        print("Transaction History: ")
        for transaction in self.transactions_history:
            Screen().line(10)
            print(f"ID: {transaction.id}\nTime: {transaction.time}\nAmount: {transaction.amount}\nTransaction Type: {transaction.type.value}")