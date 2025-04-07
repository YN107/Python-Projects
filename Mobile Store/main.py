import csv
import os
import time
import platform
import inspect
from datetime import datetime


user_admin = '''
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
║                     * Admin Menu *                      ╣
╠═════════════════════════════════════════════════════════╣
║ [1] View Phones Infos      | [2] Add New Phone          ╣
╠═════════════════════════════════════════════════════════╣
║ [3] Remove Phone           | [4] Search Phone           ╣
╠═════════════════════════════════════════════════════════╣
║ [5] Change Quantity        | [6] Change Price           ╣
╠═════════════════════════════════════════════════════════╣
║ [7] Available Phones       | [8] Out of Stock Phones    ╣
╠═════════════════════════════════════════════════════════╣
║ [9] Import Data            | [10] View Wallet           ╣ 
╠═════════════════════════════════════════════════════════╣      
╣ [11] Events History        | [12] Main Menu             ╣ 
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
║ [7] Filter Phones by Quantity  | [8] Main Menu                     ║
╚════════════════════════════════════════════════════════════════════╝
'''


set_menu = '''
╔═══════════════════════════════════════════════════╗
║                   * Settings *                    ╣
╠═══════════════════════════════════════════════════╣
║ [1] Change wallet      | [2] Zero wallet          ╣   
╠═══════════════════════════════════════════════════╣  
╣ [3] Clear History      | [4] Main Menu            ╣
╚═══════════════════════════════════════════════════╝
'''

total = 0

phones = {}

####################

def View_Phones_Infos() :
    print('-'*20)
    for i,(phone,price) in enumerate(phones.items(),1) :
        print(f'{i} - Phone : {phone}')
        print(f'Quantity: {"Out of stock" if price[0] == "0" else price[0]}')
        print(f'Price : {price[1]}')
        print('-'*20)
    add_event(inspect.currentframe().f_code.co_name, f"{datetime.now()}")



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
    elif search_by == "p":
        user_input_price = input('Enter phone price to view its information : ').lower().strip()
        if user_input_price :
            for i, (phone, price) in list(enumerate(phones.items(), 1)):
                if user_input_price == (phones[phone][1]) :
                    print('-'*20)
                    print(f'{i} - Phone : {phone}')
                    print(f'Quantity: {"Out of stock" if phones[phone][0] == "0" else phones[phone][0]}')
                    print(f'Price : {phones[phone][1]}')
                    print('-'*20)
        else:
            print('--> Invalid Input .')
    elif search_by == "q":
        user_input_quantity = input('Enter phone quantity to view its information : ').lower().strip()
        if user_input_quantity :
            for j, (phone, price) in list(enumerate(phones.items(), 1)):
                if user_input_quantity == (phones[phone][0]) :
                    print('-'*20)
                    print(f'{j} - Phone : {phone}')
                    print(f'Quantity: {"Out of stock" if phones[phone][0] == "0" else phones[phone][0]}')
                    print(f'Price : {phones[phone][1]}')
                    print('-'*20)
        else:
            print('--> Invalid Input .')
    add_event(inspect.currentframe().f_code.co_name, f"{datetime.now()}")

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
                            add_event(inspect.currentframe().f_code.co_name, f"{datetime.now()}")
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



def Remove_Phone(file_name):
    View_Phones_Infos()
    user_input = input('Enter Phone Number To Remove : ').strip().title()
    check = user_input.isdigit()
    if user_input and check:
        with open(file_name,newline='') as f :
            reader = csv.reader(f)
            lst_reader = list(reader)
            if 0 < int(user_input) <= len(lst_reader) :
                check_remove = input(f'Are You Sure You Want To Delete\n"{lst_reader[int(user_input) - 1][0]}" (y/n) ? :  ')
                if check_remove.lower() == 'y' :
                    if lst_reader[int(user_input) - 1] != [] :
                        del phones[lst_reader[int(user_input) - 1][0]]
                        del lst_reader[int(user_input) - 1]
                        print('Deleted Successfully !')
                        add_event(inspect.currentframe().f_code.co_name, f"{datetime.now()}")
                        with open(file_name,'w',newline='') as fw :
                            writer = csv.writer(fw)
                            for row in lst_reader:
                                if row:
                                    writer.writerow(row)
                else :
                    print(f'"{lst_reader[int(user_input) - 1][0]}" Still in your Phones .')
            else:
                print('--> Invalid Input .')
    else:
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
    add_event(inspect.currentframe().f_code.co_name, f"{datetime.now()}")


def Not_Available_Phones():
    print('-'*20)
    print('-'*20)
    for i,(phone,price) in enumerate(phones.items(),1) :
            if price[0] == '0' :
                print(f'{i} - Phone : {phone}')
                print(f'Quantity : Out of stock')
                print(f'Price : {price[1]}')
                print('-'*20)
    add_event(inspect.currentframe().f_code.co_name, f"{datetime.now()}")

def Import_Data(file_name):
    try:
        user_input = input("Enter Name of csv file to import data (Without index) : ")
        if user_input:
            with open(file_name,"a") as f, open(f"{user_input}.csv") as f1 :
                reader = csv.reader(f1)
                writer = csv.writer(f)
                for row in reader:
                    writer.writerow(row)
                    add_event(inspect.currentframe().f_code.co_name, f"{datetime.now()}")
                print("Done")
    except:
        print("Invalid Input")




def Change_Item_Quantity(file_name):
    View_Phones_Infos()
    user_input = input('Enter Item Number to Change its Quantity : ')
    check = user_input.isdigit()
    if user_input and check:
        with open(file_name,newline='') as f :
            lst_reader2 = list(csv.reader(f))
            if 0 < int(user_input) <= len(lst_reader2):
                with open(file_name,newline='') as f :
                    reader = csv.reader(f) 
                    lst_reader = list(reader)
                    user_input_change_q = input(f'Enter New Quantity of "{lst_reader[int(user_input) - 1][0]}"\n(The Old Quantity is "{lst_reader[int(user_input) - 1][1]}") : ')
                    check1 = user_input_change_q.isdigit()
                    if check1 and user_input_change_q :
                            lst_reader[int(user_input) - 1][1] = int(user_input_change_q)
                            phones[lst_reader[int(user_input) - 1][0]] = int(user_input_change_q)
                            print(f"{lst_reader[int(user_input) - 1][0]}'s Quantity has been Changed Successfully !")
                            add_event(inspect.currentframe().f_code.co_name, f"{datetime.now()}")
                    else:
                        print('--> Invalid Input .')
                with open(file_name,'w',newline='') as f1:
                    writer = csv.writer(f1)
                    writer.writerows(lst_reader)
            else:
                print('--> Invalid Input .')
            
    else:
        print('--> Invalid Input .')
def Change_Item_Price(file_name) :
    View_Phones_Infos()
    user_input = input('Enter Item Number to Change its Price : ')
    check = user_input.isdigit()
    if user_input and check:
        with open(file_name,newline='') as f:
            lst_reader1 = list(csv.reader(f))
            if 0 < int(user_input) <= len(lst_reader1):
                with open(file_name,newline='') as f :
                    reader = csv.reader(f) 
                    lst_reader = list(reader)
                    user_input_change_p = input(f'Enter New Price of "{lst_reader[int(user_input) - 1][0]}"\n(The Old Price is "{lst_reader[int(user_input) - 1][2]}") : ')
                    check1 = user_input_change_p.isdigit()
                    if check1 and user_input_change_p :
                        lst_reader[int(user_input) - 1][2] = int(user_input_change_p)
                        list(phones[lst_reader[int(user_input) - 1][0]])[1] = int(user_input_change_p)
                        print(f"{lst_reader[int(user_input) - 1][0]}'s Price has been Changed Successfully !")
                    else:
                        print('--> Invalid Input .')
                with open(file_name,'w',newline='') as f1:
                    writer = csv.writer(f1)
                    writer.writerows([row for row in lst_reader if any(row)])
                add_event(inspect.currentframe().f_code.co_name, f"{datetime.now()}")
            else:
                print('--> Invalid Input .')
            
    else:
        print('--> Invalid Input .')



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
                        add_event(inspect.currentframe().f_code.co_name, f"{datetime.now()}")
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
    global total
    View_wallet()
    print(10*'-')
    new_num = input(f"Enter a new number : ")
    if new_num and new_num.isdigit():
        total = float(new_num)
        View_wallet()
        print(10*'-')
        add_event(inspect.currentframe().f_code.co_name, f"{datetime.now()}")
    else:
        print("Invalid Input")

def zero_wallet():
    global total
    print(10*'-')
    View_wallet()
    print(10*'-')
    print("Done !")
    total = 0
    View_wallet()
    add_event(inspect.currentframe().f_code.co_name, f"{datetime.now()}")

def Filter_phones_price():
    print('-'*20)
    try:
        min_price = float(input("Enter minimum price : "))
        max_price = float(input("Enter maximum price : "))
        sorted_phones = sorted(phones.items(), key=lambda x: float(x[1][1]))
        print('-'*20)
        for phone,price in sorted_phones :
            if (min_price) <= float(price[1]) <= (max_price):
                print(f'{list(phones.keys()).index(phone) + 1} - Phone : {phone}')
                print(f'Quantity: {"Out of stock" if price[0] == "0" else price[0]}')
                print(f'Price : {price[1]}')
                print('-'*20)
        add_event(inspect.currentframe().f_code.co_name, f"{datetime.now()}")
    except Exception:
        print('-'*10)
        print("ERROR")
def Filter_phones_quantity():
    print('-'*20)
    try:
        min_q = float(input("Enter minimum quantity : "))
        max_q = float(input("Enter maximum quantity : "))
        sorted_phones = sorted(phones.items(), key=lambda x: float(x[1][0]))
        print('-'*20)
        for phone,price in sorted_phones :
            if (min_q) <= float(price[0]) <= (max_q):
                print(f'{list(phones.keys()).index(phone) + 1} - Phone : {phone}')
                print(f'Quantity: {"Out of stock" if price[0] == "0" else price[0]}')
                print(f'Price : {price[1]}')
                print('-'*20)
        add_event(inspect.currentframe().f_code.co_name, f"{datetime.now()}")
    except Exception:
        print('-'*10)
        print("ERROR")

def Clear_History():
        with open("history.txt","w") as f:
            f.write(f"")
        print("Done!")

def View_history():
    with open("history.txt") as f:
        print("-"*15)
        print(f.read().strip())

def add_event(event,time):
    with open("history.txt","a") as f:
        f.write(f"{event} - {time}\n----------------\n")

def View_wallet():
    global total
    print(10*'-')
    print(f"Wallet : ${total}")
    add_event(inspect.currentframe().f_code.co_name, f"{datetime.now()}")

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


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main(file_name):
    start = time.time()
    load_data(file_name)
    clear()
    while True:
        input('-------\nPRESS ENTER : ')
        clear()
        print(user_admin.strip())
        user_input_menu = input(": ").lower().strip()
        if user_input_menu == "1" :
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
                    Remove_Phone(file_name)
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
                elif user_input == '12' :
                    break
                else :
                    print('-------')
                    print('--> Invalid Input .')
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
                    break
        elif user_input_menu == "3":
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
            exit()
        else :
            print('-------')
            print('--> Invalid Input .')

clear()
while True:
    try:
        file = input("ENTER FILE NAME (without index) : ")
        main(f"{file}.csv")
        break  
    except Exception:
        print(f"There is no file named '{file}.csv'")

# BY YAHIA