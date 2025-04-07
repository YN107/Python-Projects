import time
from authenticator import Authenticator
class CardReader:
    def __init__(self,atm):
        self.atm = atm
        self.Authenticator = Authenticator(self.atm.bank)
    def insert_card(self,card):
        view_PIN = True
        i = 3
        j = 3
        self.atm.screen.clear()
        while (i > 0):
            self.atm.screen.line(27)
            pin = self.atm.keypad.get_input("1. View PIN\n---------\n2. Quit\n---------\nPlease Enter Card PIN: ", view_PIN)
            self.atm.screen.line(27)
            if pin == "1":
                self.atm.screen.clear()
                j += 1
                view_PIN = False
                continue
            if pin == "2":
                quit()
                self.insert_card(card)
            account = self.Authenticator.authenticate(card.number,pin)
            if account:
                self.atm.main_menu(account)
            else:
                self.atm.screen.clear()
                self.atm.screen.line(7)
                self.atm.screen.error(f"Invalid PIN\n{i - 1} attempt(s) remaining.")
                i -= 1
        self.atm.screen.clear()
        self.atm.screen.line(7)
        self.atm.screen.show_message("Too many incorrect attempts. Please try again later.")
        time.sleep(4)
        self.atm.screen.line(10)
        self.atm.screen.show_message("Leaving...")
        time.sleep(3)
        return None
