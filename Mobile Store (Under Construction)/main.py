import csv
import os
import time
import inspect
from datetime import datetime
import getpass


main_menu = '''
╔════════════════════════════════╗
║            * Menu *            ║
╠════════════════════════════════╣
║ [1] Admin                      ║
║ [2] User Services              ║
║ [3] Settings                   ║
║ [4] Quit                       ║
╚════════════════════════════════╝
'''


admin_menu = '''
╔═════════════════════════════════════════════════════════╗
║                     * Admin Menu *                      ║
╠═════════════════════════════════════════════════════════╣
║ [1] View Phones Infos      | [2] Add New Phone          ║
╠═════════════════════════════════════════════════════════╣
║ [3] Delete Phone           | [4] Search Phone           ║
╠═════════════════════════════════════════════════════════╣
║ [5] Change Quantity        | [6] Change Price           ║
╠═════════════════════════════════════════════════════════╣
║ [7] Available Phones       | [8] Out of Stock Phones    ║
╠═════════════════════════════════════════════════════════╣
║ [9] Import Data            | [10] View Wallet           ║ 
╠═════════════════════════════════════════════════════════╣      
║ [11] View Events History   | [12] Add Password          ║
╠═════════════════════════════════════════════════════════╣ 
║ [13] View All Passwords    | [14] Delete All Passwords  ║
╠═════════════════════════════════════════════════════════╣ 
║ [15] Main Menu                                          ║
╚═════════════════════════════════════════════════════════╝
'''

user_menu = '''
╔════════════════════════════════════════════════════════════════════╗
║                      * User Services Menu *                        ║
╠════════════════════════════════════════════════════════════════════╣
║ [1] View Phones Infos          | [2] Search Phone                  ║
╠════════════════════════════════════════════════════════════════════╣
║ [3] Available Phones           | [4] Out of Stock Phones           ║
╠════════════════════════════════════════════════════════════════════╣
║ [5] Sell Phone                 | [6] Filter Phones by Price        ║   
╠════════════════════════════════════════════════════════════════════╣   
║ [7] Filter Phones by Quantity  | [8] Top Selling Phones            ║
╠════════════════════════════════════════════════════════════════════╣
║ [9] Main Menu                                                      ║
╚════════════════════════════════════════════════════════════════════╝
'''


set_menu = '''
╔═══════════════════════════════════════════════════╗
║                   * Settings *                    ║
╠═══════════════════════════════════════════════════╣
║ [1] Change wallet      | [2] Zero wallet          ║   
╠═══════════════════════════════════════════════════╣  
║ [3] Clear History      | [4] Main Menu            ║
╚═══════════════════════════════════════════════════╝
'''

total = 0

phones = {}

passwords = {}

####################

# Top Selling Phones (USER)
# Phone Recommendation (USER)
# CART (USER
# Rename Phone (ADMIN)

def load_data(file_name):
    with open(file_name,'r',newline='') as f1 :
        read = csv.reader(f1)
        lst_read = list(read)
        for row in lst_read :
            if lst_read:
                if row :
                    phones.update({row[0] : [row[1],row[2]]})
    with open(file_name,'w',newline='') as f1 :
        for phone,info in phones.items() :
            writer = csv.writer(f1)
            writer.writerow([phone,info[0],info[1]])

def View_Phones_Infos() :
    print('-'*20)
    for i,(phone,price) in enumerate(phones.items(),1) :
        print(f'{i} - Phone : {phone}')
        print(f'Quantity: {"Out of stock" if price[0] == "0" else price[0]}')
        print(f'Price : {price[1]}')
        print('-'*20)
    add_event(inspect.currentframe().f_code.co_name)



def Search_Phone():
    search_by = input("Search by (n - p - q) : ").lower().strip()
    if search_by == "n":
        user_input = input('Enter phone name to view its information: ').lower().strip()
        if user_input:
            for l,n in enumerate(list(phones.keys()),1):
                if user_input in n:
                    q,p = phones[n]
                    print('-'*20)
                    print(f'{l} - Phone : {n}')
                    print(f'Quantity: {"Out of stock" if q == "0" else q}')
                    print(f'Price : {p}')
                    print('-'*20)
            add_event("search_phone_by_name")
    elif search_by == "p":
        user_input_price = input('Enter phone price to view its information : ').lower().strip()
        if user_input_price :
            for i, (phone, pricee) in list(enumerate(phones.items(), 1)):
                if user_input_price == (pricee[1]) :
                    print('-'*20)
                    print(f'{i} - Phone : {phone}')
                    print(f'Quantity: {"Out of stock" if pricee[0] == "0" else pricee[0]}')
                    print(f'Price : {pricee[1]}')
                    print('-'*20)
            add_event("search_phone_by_price")
        else:
            print('--> Invalid Input .')
    elif search_by == "q":
        user_input_quantity = input('Enter phone quantity to view its information : ').lower().strip()
        if user_input_quantity :
            for j, (phone, price) in list(enumerate(phones.items(), 1)):
                if user_input_quantity == (price[0]) :
                    print('-'*20)
                    print(f'{j} - Phone : {phone}')
                    print(f'Quantity: {"Out of stock" if price[0] == "0" else price[0]}')
                    print(f'Price : {price[1]}')
                    print('-'*20)
            add_event("search_phone_by_quantity")
        else:
            print('--> Invalid Input .')
    

def Add_Phone(file_name) :
    keys = phones.keys()
    user_input = input('Enter Phone Name To add to your phones : ').lower().strip().split()
    if " ".join(user_input) :
        if " ".join(user_input) not in list(keys) :
            user_input_quantity = input(f'Enter quantity of "{" ".join(user_input)}" : ').title()
            check = user_input_quantity.isdigit()
            if check and user_input_quantity:
                user_input_price = input(f'Enter price of "{" ".join(user_input)}" : ')
                check_2 = user_input_price.isdigit()
                if check_2 and user_input_price:
                    with open(file_name, 'a',newline='') as f :
                            f.write(f'{" ".join(user_input)},{user_input_quantity},{user_input_price}\n')
                            phones[" ".join(user_input)] = [user_input_quantity,user_input_price]
                            print(20*'-')
                            print(f'"{" ".join(user_input)}" has been added Successfully !')
                            add_event(f"{inspect.currentframe().f_code.co_name}(Phone: {user_input[0]})")
                else:
                    print('--> Invalid Input .')
            else:
                print('--> Invalid Input .')    
        else:
            print("-"*10)
            print('Invalid Input\nYou already have phone with this name')
            print("-"*10)
            print((f"{list(phones.keys()).index(" ".join(user_input)) + 1} - {" ".join(user_input)}\nQuantity : {phones[" ".join(user_input)][0]}\nPrice : {phones[" ".join(user_input)][1]}") if phones[" ".join(user_input)][0] != "0" else (f"{list(phones.keys()).index(" ".join(user_input)) + 1} - {" ".join(user_input)}\nQuantity : Out of Stock\nPrice : {phones[" ".join(user_input)][1]}"))
    else:
        print('--> Invalid Input .')



def Delete_Phone(file_name):
    View_Phones_Infos()
    print("-"*10)
    user_input = input('Enter Phone Number To Remove : ').strip().title()
    check = user_input.isdigit()
    if user_input and check:
        with open(file_name,newline='') as f :
            reader = csv.reader(f)
            lst_reader = list(reader)
            if 0 < int(user_input) <= len(lst_reader) :
                print("-"*10)
                check_remove = input(f'Are You Sure You Want To Delete\n"{lst_reader[int(user_input) - 1][0]}" (y/n) ? :  ')
                if check_remove.lower() == 'y' :
                    if lst_reader[int(user_input) - 1] != [] :
                        add_event(f"{inspect.currentframe().f_code.co_name}(Phone: {lst_reader[int(user_input) - 1][0]})")
                        del phones[lst_reader[int(user_input) - 1][0]]
                        del lst_reader[int(user_input) - 1]
                        print("-"*10)
                        print('Deleted Successfully !')
                        with open(file_name,'w',newline='') as fw :
                            writer = csv.writer(fw)
                            for row in lst_reader:
                                if row:
                                    writer.writerow(row)
                else :
                    print("-"*10)
                    print(f'"{lst_reader[int(user_input) - 1][0]}" Still in your Phones .')
            else:
                print("-"*10)
                print('--> Invalid Input .')
    else:
        print("-"*10)
        print('--> Invalid Input .')
                
def Available_Phones():
    print('-'*20)
    print('-'*20)
    for i,(phone,price) in enumerate(phones.items(),1) :
            if price[0] != '0' :
                print(f'{i} - Phone : {phone}')
                print(f'Quantity : {price[0]}')
                print(f'Price : {price[1]}')
                print('-'*20)
    add_event(inspect.currentframe().f_code.co_name)


def Not_Available_Phones():
    print('-'*20)
    for i,(phone,price) in enumerate(phones.items(),1) :
            if price[0] == '0' :
                print(f'{i} - Phone : {phone}')
                print(f'Quantity : Out of stock')
                print(f'Price : {price[1]}')
                print('-'*20)
    add_event("Out_of_stock_phones")

def Import_Data(file_name):
    try:
        user_input = input("Enter Name of csv file to import data (Without index) : ")
        if user_input:
            with open(file_name,"a") as f, open(f"{user_input}.csv") as f1 :
                reader = csv.reader(f1)
                writer = csv.writer(f)
                for row in reader:
                    writer.writerow(row)
                    add_event(inspect.currentframe().f_code.co_name)
                print("Done")
    except:
        print("Invalid Input")




def Change_Item_Quantity(file_name):
    try:
        View_Phones_Infos()
        user_input = input('Enter Item Number to Change its Quantity : ')
        if user_input and user_input.isdigit():
            print('-'*10)
            with open(file_name,newline='') as f :
                read = csv.reader(f)
                lst_reader = list(read)
                new_q = int(input(f'Enter New Quantity of {lst_reader[int(user_input) - 1][0]},\n(The Old Quantity is "{lst_reader[int(user_input)-1][1]}"): '))
                if new_q >= 0:
                    add_event(f"{inspect.currentframe().f_code.co_name}(Phone: {lst_reader[int(user_input) - 1][0]}, Old_Quantity: {lst_reader[int(user_input)-1][1]}, New_Quantity: {new_q})")
                    lst_reader[int(user_input)-1][1] = new_q
                    with open(file_name,'w',newline='') as f1:
                        writer = csv.writer(f1)
                        writer.writerows([row for row in lst_reader if any(row)])
                    load_data(file_name)
                    print('-'*10)
                    print("Quantity Changed Successfully !")
                else:
                    print("-"*10)
                    print("Invalid Input")
        else:
            print("-"*10)
            print("Invalid Input")
    except Exception:
        print("-"*20)
        print("Invalid Input")
            
def Change_Item_Price(file_name) :
    try:
        View_Phones_Infos()
        user_input = input('Enter Item Number to Change its Price : ')
        if user_input and user_input.isdigit():
            print('-'*10)
            with open(file_name,newline='') as f :
                read = csv.reader(f)
                lst_reader = list(read)
                new_p = int(input(f'Enter New Price of {lst_reader[int(user_input) - 1][0]},\n(The Old Price is "{lst_reader[int(user_input)-1][2]}"): '))
                if new_p >= 0:
                    add_event(f"{inspect.currentframe().f_code.co_name}(Phone: {lst_reader[int(user_input) - 1][0]}, Old_Price: {lst_reader[int(user_input)-1][2]}, New_Price: {new_p})")
                    lst_reader[int(user_input)-1][2] = new_p
                    with open(file_name,'w',newline='') as f1:
                        writer = csv.writer(f1)
                        writer.writerows([row for row in lst_reader if any(row)])
                    load_data(file_name)
                    print('-'*10)
                    print("Price Changed Successfully !")
                else:
                    print("-"*10)
                    print("Invalid Input")
        else:
            print("-"*10)
            print("Invalid Input")
    except Exception:
        print("-"*20)
        print("Invalid Input")


def Top_selling_phones():
    with open("top_selling_phones.csv",newline="") as f:
        reader = csv.reader(f)
        lst_reader = list(reader)
        print(lst_reader)


def add_top_selling_phone(phone):
    with open("top_selling_phones.csv","a",newline="") as f:
        f.write(f"{phone}\n")

def Sell_phone(file_name) :
    global total
    Available_Phones()
    user_input = input('Enter Phone Number to sell : ')
    check = user_input.isdigit()
    if user_input and check :
        if 0 < int(user_input) <= len(phones) :
            with open(file_name) as f:
                reader = csv.reader(f)
                lst_reader = list(reader)
                if phones[lst_reader[int(user_input) - 1][0]][0] != '0' :
                    quantity = input("Enter the quantity you want to sell : ")
                    if quantity.isdigit() and quantity and int(quantity) <= int(phones[lst_reader[int(user_input) - 1][0]][0]):
                        phones[lst_reader[int(user_input) - 1][0]][0] = str(int(phones[lst_reader[int(user_input) - 1][0]][0]) - int(quantity))
                        price = float(lst_reader[int(user_input) - 1][2]) * int(quantity)
                        total += price 
                        print(10*'-')
                        print(f"${price} added to your wallet !")
                        print(10*'-')
                        print(f'Done !')
                        add_top_selling_phone(lst_reader[int(user_input) - 1][0])
                        add_event(f"{inspect.currentframe().f_code.co_name}(Phone: {lst_reader[int(user_input) - 1][0]}, Quantity: {quantity})")
                    else:
                        print("Invalid Input")
                else:
                    print(f"Invalid Input")
                with open(file_name, 'w', newline='') as f:
                    writer = csv.writer(f)
                    for phone, info in phones.items():
                        writer.writerow([phone,info[0],info[1]])
    else:
        print('--> Invalid Input .')

def change_wallet():
    try:
        global total
        View_wallet()
        print(10*'-')
        new_num = float(input(f"Enter New Wallet : "))
        if new_num:
            total = new_num
            print(10*'-')
            print("Done !")
            add_event(f"{inspect.currentframe().f_code.co_name}(Wallet: {total})")
        else:
            print("Invalid Input")
    except Exception:
        print(10*'-')
        print("Invalid Input")

def zero_wallet():
    global total
    print(10*'-')
    print("Done !")
    total = 0
    add_event(inspect.currentframe().f_code.co_name)

def Filter_phones_price():
    print('-'*20)
    try:
        min_price = float(input("Enter minimum price : "))
        max_price = float(input("Enter maximum price : "))
        if max_price > min_price:
            sorted_phones = sorted(phones.items(), key=lambda x: float(x[1][1]))
            print('-'*20)
            for phone,price in sorted_phones :
                if (min_price) <= float(price[1]) <= (max_price):
                    print(f'{list(phones.keys()).index(phone) + 1} - Phone : {phone}')
                    print(f'Quantity: {"Out of stock" if price[0] == "0" else price[0]}')
                    print(f'Price : {price[1]}')
                    print('-'*20)
            add_event(f"Filter_phones_by_price(Min_price: {min_price}, Max_price: {max_price})")
        else:
            print('-'*20)
            print("maximum price should be > minimum price")
    except Exception:
        print('-'*10)
        print("Invalid Input")
def Filter_phones_quantity():
    print('-'*20)
    try:
        min_q = int(input("Enter minimum quantity : "))
        max_q = int(input("Enter maximum quantity : "))
        if max_q > min_q:
            sorted_phones = sorted(phones.items(), key=lambda x: int(x[1][0]))
            print('-'*20)
            for phone,price in sorted_phones :
                if (min_q) <= int(price[0]) <= (max_q):
                    print(f'{list(phones.keys()).index(phone) + 1} - Phone : {phone}')
                    print(f'Quantity: {"Out of stock" if price[0] == "0" else price[0]}')
                    print(f'Price : {price[1]}')
                    print('-'*20)
            add_event(f"Filter_phones_by_quantity(Min_quantity: {min_q}, Max_quantity: {max_q})")
        else:
            print('-'*20)
            print("maximum quantity should be > minimum quantity")
    except Exception:
        print('-'*10)
        print("ERROR")

def Clear_History():
    with open("history.txt","w") as f:
        f.write(f"")
    print('-'*10)
    print("Done!")

def View_history():
    with open("history.txt") as f:
        print("-"*15)
        print(f.read().strip())

def add_event(event):
    with open("history.txt","a") as f:
        f.write(f"{event} - {datetime.now()}\n----------------\n")

def View_wallet():
    global total
    print(10*'-')
    print(f"Wallet : ${total}")
    add_event(f"{inspect.currentframe().f_code.co_name}(${total})")



def load_pass():
    with open("passwords.csv",'r',newline='') as f1 :
        read = csv.reader(f1)
        lst_read = list(read)
        for row in lst_read :
            if lst_read:
                if row :
                    passwords.update({row[0] : row[1]})
    with open("passwords.csv",'w',newline='') as f1 :
        for pas,date in passwords.items() :
            writer = csv.writer(f1)
            writer.writerow([pas, date])

def add_new_password():
        print(20*'-')
        new_pass = getpass.getpass("Enter The Password: ")
        if new_pass:
            if 2 < len(new_pass) < 8:
                with open("passwords.csv", 'a',newline='') as f :
                    f.write(f'{new_pass}, {datetime.now()}\n')
                with open("passwords.csv", 'r',newline='') as f1 :
                    read = csv.reader(f1)
                    lst_read = list(read)
                    for row in lst_read :
                        if lst_read:
                            if row :
                                passwords.update({row[0]: row[1]})
                    print(20*'-')
                    print('Password added Successfully !')
                    add_event(inspect.currentframe().f_code.co_name)
            else:
                print(20*'-')
                print("Password should be 2-8 characters long")
        else:
            print(20*'-')
            print("--> Invalid Input")


def add_password():
    with open("passwords.csv", 'r',newline='') as f1 :
        read = csv.reader(f1)
        lst_read = list(read)
        if not lst_read:
            add_new_password()
        else:
            print(20*'-')
            conf_pass = getpass.getpass("Enter The Old Password: ")
            if conf_pass and conf_pass == lst_read[-1][0]:
                add_new_password()
            else:
                print(20*'-')
                print("Invalid Password")


def view_password():
    if passwords:
        print(20*'-')
        enter_pass = getpass.getpass("Enter The Password: ")
        if enter_pass == list(passwords.keys())[-1]:
            print("-"*20)
            for pas, date in passwords.items():
                print(f"Password: {pas}\nDate: {date}\n{'-'*20}")
            add_event(inspect.currentframe().f_code.co_name)
        else:
            print(20*'-')
            print("Invalid Password")
    else:
        print(20*'-')
        print("There are no passwords yet !")


def del_passwords():
    print(20*'-')
    if not passwords:
        print("There are no passwords to delete !")
    else:
        enter_pass = getpass.getpass("Enter The Password: ")
        if enter_pass == list(passwords.keys())[-1]:
            with open("passwords.csv", "w",newline="") as f:
                f.truncate(0)
            passwords.clear()
            load_pass()
            print(20*'-')
            print("Deleted Successfully !")
            add_event("Delete_all_passwords")
        else:
            print(20*'-')
            print("Invalid Password")


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def admin(file_name):
    while True:
        input('-------\nPRESS ENTER : ')
        clear()
        print(admin_menu.strip())
        user_input = input(": ")
        if user_input == '1' :
            View_Phones_Infos()
        elif user_input == '2' :
            Add_Phone(file_name)
        elif user_input == '3' :
            Delete_Phone(file_name)
        elif user_input == '4' :
            Search_Phone()
        elif user_input == '5' :
            Change_Item_Quantity(file_name)
        elif user_input == '6' :
            Change_Item_Price(file_name)
        elif user_input == '7':
            Available_Phones()
        elif user_input == "8":
            Not_Available_Phones()
        elif user_input == "9":
            Import_Data(file_name)
        elif user_input == "10":
            View_wallet()
        elif user_input == "11":
            View_history()
        elif user_input == "12":
            add_password()
        elif user_input == "13":
            view_password()
        elif user_input == "14":
            del_passwords()
        elif user_input == '15' :
            break
        else :
            print('-------')
            print('--> Invalid Input .')

def main(file_name):
    start = time.time()
    load_data(file_name)
    load_pass()
    clear()
    while True:
        input('-------\nPRESS ENTER : ')
        clear()
        print(main_menu.strip())
        user_input_menu = input(": ").lower().strip()
        if user_input_menu == "1" :
            if passwords:
                print(20*'-')
                enter_pass = getpass.getpass("Enter The Password: ")
                if enter_pass == list(passwords.keys())[-1]:
                    admin(file_name)
                else:
                    print(20*'-')
                    print("Invalid Password")
                    continue
            else:
                admin(file_name)
        elif user_input_menu == "2":
            while True:
                input('-------\nPRESS ENTER : ')
                clear()
                print(user_menu.strip())
                user_input1 = input(": ")
                if user_input1 == "1":
                    View_Phones_Infos()
                elif user_input1 == "2":
                    Search_Phone()
                elif user_input1 == "3":
                    Available_Phones()
                elif user_input1 == "4":
                    Not_Available_Phones()
                elif user_input1 == "5":
                    Sell_phone(file_name)
                elif user_input1 == "6":
                    Filter_phones_price()
                elif user_input1 == "7":
                    Filter_phones_quantity()
                elif user_input1 == "8":
                    Top_selling_phones()
                elif user_input1 == "9":
                    break
        elif user_input_menu == "3":
            if passwords:
                print(20*'-')
                enter_pass = getpass.getpass("Enter The Password: ")
                if enter_pass == list(passwords.keys())[-1]:
                    clear()
                    print(set_menu.strip())
                    user_input_set = input(": ")
                    if user_input_set == "1":
                        change_wallet()
                    elif user_input_set == "2":
                        zero_wallet()
                    elif user_input_set == "3":
                        Clear_History()
                    elif user_input_set == "4":
                        continue
                else:
                    print(20*'-')
                    print("Invalid Password")
                    continue
            else:
                clear()
                print(set_menu.strip())
                user_input_set = input(": ")
                if user_input_set == "1":
                    change_wallet()
                elif user_input_set == "2":
                    zero_wallet()
                elif user_input_set == "3":
                    Clear_History()
                elif user_input_set == "4":
                    continue
        elif user_input_menu == "4":
            end = time.time()
            timee = end - start
            timee /= 60
            print("-"*5)
            View_wallet()
            time.sleep(2)
            print("-"*5)
            print(f"In {timee:.2f} minutes !")
            print("-"*5)
            time.sleep(2)
            print('Leaving...')
            time.sleep(2.5)
            add_event("Quit")
            exit()
        else :
            print('-------')
            print('--> Invalid Input .')

clear()
while True:
    try:
        print(20*'-')
        file = input("ENTER FILE NAME (without index) : ")
        main(f"{file}.csv")
        break  
    except Exception:
        print(20*'-')
        print(f"There is no file named '{file}.csv'")

# BY YAHIA