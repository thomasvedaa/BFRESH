from functions_customer import *
from functions_car import *

connection=sqlite3.connect('rental_database.sqlite')

def modify_car_menu():
    while True:
        modify_car = int(input("1. Add car \n2. Edit car \n3. Remove car \n4. Exit"))
        if modify_car == 1:
            add_car_to_database(connection)
        elif modify_car == 2:
            pass
        elif modify_car == 3:
            pass
        elif modify_car==4:
            break
        else:
            print("Enter a valid number")

def modify_customer_menu():
    while True:
        modify_customer = int(input("1. Add customer \n2. Edit customer \n3. Remove customer \n4. Exit"))
        if modify_customer == 1:
            add_customer_to_database(connection)
        elif modify_customer == 2:
            pass
        elif modify_customer == 3:
            pass
        elif modify_customer==4:
            break
        else:
            print("Enter a valid number")
