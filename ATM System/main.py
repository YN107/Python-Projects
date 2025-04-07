from atm import ATMInterface
from account import Account
from card import Card
from bank import Bank
from customer import Customer
from cardReader import CardReader

def main():
    bank = Bank("HSBC","242")
    atm1 = ATMInterface(bank,"cairo")
    customer1 = Customer('Yahia',"sohag","34467547548", "yahia7773332021@gmail.com")
    customer2 = Customer('Ashraf',"sohag","09023345", "ashraf2342@gmail.com")
    acc1 = Account("654321")
    acc2 = Account("123456")
    card1 = Card("86567802","0000")
    card2 = Card("5776879","8888")

    customer1.add_account(acc1)
    customer2.add_account(acc2)
    bank.add_customer(customer1)
    bank.add_customer(customer2)
    acc1.add_card(card1)
    acc2.add_card(card2)

    CardReader(atm1).insert_card(card1)

if __name__ == "__main__":
    main()