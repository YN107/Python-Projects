from screen import Screen
from transactions import *

class WithdrawHandler:
    def __init__(self,screen,keypad):
        self.keypad = keypad
        self.screen = screen

    def handle(self,account):
        while True:
            self.screen.line(8)
            try:
                amount = int(self.keypad.get_input("Enter Amount To Withdraw: "))
                if account.balance >= amount :
                    if amount > 0 :
                        transaction = WithdrawTrs(amount)
                        transaction.execute(account)
                    else:
                        Screen().line(10)
                        Screen().error("Amount must be > 0")
                else:
                    Screen().line(10)
                    Screen().error("Insufficient funds")
                break
            except Exception :
                self.screen.line(8)
                self.screen.show_message("Invalid Input.")
                break

class DepositHandler:
    def __init__(self,screen,keypad):
        self.keypad = keypad
        self.screen = screen

    def handle(self,account):
        while True:
            self.screen.line(8)
            try:
                amount = int(self.keypad.get_input("Enter Amount To Deposite: "))
                if amount > 0 :
                    transaction = DepositTrs(amount)
                    transaction.execute(account)
                    break
                else:
                    Screen().line(10)
                    Screen().error("Amount must be > 0")
                    break
            except Exception :
                self.screen.line(8)
                self.screen.show_message("Invalid Input.")
                break

class BalanceInquiryHandler:
    def handle(self,account):
        transaction = BalanceInquiryTrs()
        transaction.execute(account)

class ViewTransactionsHandler:
    def handle(self,account):
        account.display_transactions_history()

class ChangeCardPinHandler:
    def handle(self, account):
        account.card.set_PIN()

class TransferFundsHandler:
    def __init__(self,screen,keypad, bank):
        self.keypad = keypad
        self.screen = screen
        self.bank = bank

    def handle(self, account):
        while True:
            try:
                self.screen.line(8)
                amount = int(self.keypad.get_input("Enter Amount To Transfer: "))
                if amount >= 0 :
                    self.screen.line(8)
                    destination_account_number = self.keypad.get_input("Enter Destination Account Number: ")
                    transaction = TransferFundsTrs(amount, destination_account_number)
                    transaction.execute(account, self.bank)
                    break
                else:
                    self.screen.line(8)
                    self.screen.show_message("Amount must be > 0")
                    break
            except Exception:
                self.screen.line(8)
                self.screen.error("Invalid Input")
                break