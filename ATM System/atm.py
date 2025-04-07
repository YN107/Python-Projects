from keypad import Keypad
from screen import Screen
from handlers import *
from cardReader import CardReader
import time

class ATMInterface:
    def __init__(self, bank, location):
        self.bank = bank
        self.loac = location
        self.keypad = Keypad()
        self.screen = Screen()
        self.WithdrawHandler = WithdrawHandler(self.screen, self.keypad)
        self.DepositHandler = DepositHandler(self.screen, self.keypad)
        self.BalanceInquiryHandler = BalanceInquiryHandler()
        self.ViewTransactionsHandler = ViewTransactionsHandler()
        self.ChangeCardPinHandler = ChangeCardPinHandler()
        self.TransferFundsHandler = TransferFundsHandler(self.screen, self.keypad, self.bank)
    def main_menu(self,account):
        self.screen.line(7)
        self.keypad.get_input("PRESS ENTER: ")
        self.screen.clear()
        main_menu ='''--------------------------------
1. Withdraw Transaction
--------------------------------
2. Deposit Transaction
--------------------------------
3. Balance Inquiry Transaction
--------------------------------
4. View Transactions
--------------------------------
5. Change Card PIN
--------------------------------
6. Transfer Funds
--------------------------------
7. Quit
--------------------------------
: '''
        while True:
            check = self.keypad.get_input(main_menu)
            match check:
                case "1":
                    self.WithdrawHandler.handle(account)
                case "2":
                    self.DepositHandler.handle(account)
                case "3":
                    self.BalanceInquiryHandler.handle(account)
                case "4":
                    self.ViewTransactionsHandler.handle(account)
                case "5":
                    self.ChangeCardPinHandler.handle(account)
                case "6":
                    self.TransferFundsHandler.handle(account)
                case "7":
                    self.screen.line(8)
                    self.screen.show_message("Ejecting Card...")
                    time.sleep(2)
                    CardReader(self).insert_card(account.card)
                case _:
                    self.screen.error("Invalid Choice")
            self.screen.line(8)
            self.keypad.get_input("PRESS ENTER: ")
            self.screen.clear()
