import sqlite3
from menu_functions import *
from functions_customer import *
from functions_car import *
from car_to_customer_functions import *


connection=sqlite3.connect('rental_database.sqlite')
while True:
    print("1. Add/Modify car\n2. Add/Modify customer\n3. Assign car to customer\n4. Unassign car to customer"
          "\n5. Show statistics\n6. Export all information to a file\n7. Import all information from a file\n8. Exit")
    choice= int(input())

    if choice==1:
        modify_car_menu()
    if choice==2:
        modify_customer_menu()
    if choice==3:
        pass
    if choice==4:
        pass
    if choice==5:
        pass
    if choice==6:
        pass
    if choice==7:
        pass
    if choice==8:
        break
