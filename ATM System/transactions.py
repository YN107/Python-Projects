from screen import Screen
from keypad import Keypad
from abc import ABC, abstractmethod
import uuid
import datetime
from transactionsTypes import TransactionsTypes
from bank import Bank

class Transaction(ABC):
    def __init__(self, type, amount=None):
        self.id = uuid.uuid4()
        self.time = datetime.datetime.now()
        self.type = type
        self.amount = amount
    @abstractmethod
    def execute(self):
        ...

class WithdrawTrs(Transaction):
    def __init__(self,amount):
        super().__init__(TransactionsTypes.WITHDRAW,amount)
    def execute(self,account):
            account.balance -= self.amount
            Screen().line(10)
            print(f"Withdrawl Successful. New Balance: ${account.balance}")
            account.add_trs(self)



class DepositTrs(Transaction):
    def __init__(self, amount):
        super().__init__(TransactionsTypes.DEPOSIT, amount)
    def execute(self,account):
        account.balance += self.amount
        Screen().line(10)
        print(f"Deposit Successful. New Balance: ${account.balance}")
        account.add_trs(self)


class BalanceInquiryTrs(Transaction):
    def __init__(self):
        super().__init__(TransactionsTypes.BALANCE_INQUIRY)
    def execute(self,account):
        Screen().line(5)
        print(f"Balance: ${account.balance}")
        self.amount = account.balance
        account.add_trs(self)


class TransferFundsTrs(Transaction):
    def __init__(self, amount, destination_account_number):
        super().__init__(TransactionsTypes.TRANSFER, amount)
        self.destination_account_number = destination_account_number
    def execute(self, account, bank):
        if account.balance >= self.amount:
            destination_account = bank.accounts.get(self.destination_account_number)
            if destination_account:
                account.balance -= self.amount
                destination_account.balance += self.amount
                Screen().line(8)
                Screen().show_message(f"Transfer Successful. New balance: {account.balance}")
                account.add_trs(self)
                destination_account.add_trs(self)
            else:
                Screen().line(8)
                Screen().show_message("Destination account not found")
        else:
            Screen().line(8)
            Screen().show_message("Insuficient funds")