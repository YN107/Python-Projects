from screen import Screen
from keypad import Keypad
class Card:
    def __init__(self, number, pin): 
        self.number = number
        self.__pin = pin
    def __str__(self):
        return f"Card Number: {self.number},PIN: {self.pin}"

    def get_PIN(self):
        return self.__pin

    def set_PIN(self):
        Screen().line(8)
        old_PIN = Keypad().get_input("Enter Old PIN: ", True)
        if self.__pin == old_PIN:
            Screen().line(8)
            new_PIN = Keypad().get_input("Enter New PIN: ", True)
            Screen().line(10)
            confirm_new_PIN = Keypad().get_input("Confirm New PIN: ", True)
            if new_PIN == confirm_new_PIN:
                self.__pin = new_PIN
                Screen().line(8)
                Screen.show_message(f"PIN Changed Successfuly, New PIN: {self.get_PIN()}")
                return True
            else:
                Screen().line(8)
                Screen().show_message("PINs dont match")
                return False
        else:
            Screen().line(8)
            print("Invalid PIN")
            return False