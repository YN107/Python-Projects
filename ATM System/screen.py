import os
class Screen:
    def show_message(self,message):
        print(f"--> {message}")
    def clear(self):
        os.system("cls" if os.name == "nt" else "clear")
    def line(self,num):
        print("-"*num)
    def error(self,error="Undefined Error"):
        print(f"Error: '{error}'")