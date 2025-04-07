from enum import Enum
class TransactionsTypes(Enum):
    WITHDRAW = "Withdraw"
    DEPOSIT = "Deposit"
    BALANCE_INQUIRY = "Balance Inquiry"
    TRANSFER = "Transfer"