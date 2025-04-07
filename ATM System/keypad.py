import getpass

class Keypad:
    def get_secure_input(self,message):
        return getpass.getpass(message)
    def get_input(self, message, secure=False):
        if secure:
            return self.get_secure_input(message)
        return input(message)