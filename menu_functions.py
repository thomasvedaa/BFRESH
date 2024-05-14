from functions_customer import *
from functions_car import *
from functions_stats import *
from assign_function import *

db = 'rental_database.sqlite'

class Main_menu:
    def menu(self):
        while True:
            print("1. Add/Modify car\n2. Add/Modify customer\n3. Assign car to customer\n4. Show statistics\n5. Export all information to a file\n"
                  "5. Import all information from a file\n7. Exit")
            choice= int(input())

            if choice==1:
                car_menu.modify_car_menu()
            if choice==2:
                customer_menu.modify_customer_menu()
            if choice==3:
                assign_car.assign_menu()
            if choice==4:
                stats.show_stats_menu()
            if choice==5:
                pass
            if choice==6:
                pass
            if choice==7:
                break




car_menu= Cars(db)
customer_menu = Customers(db)
stats=Stats(db)
assign_car=Assign_car(db)
main=Main_menu()


def search_customer():
    while True:
        search_choice = int(input("1. Search for a customer \n2. Exit\n"))
        if search_choice == 1:
            pass
        elif search_choice == 2:
            break
        else:
            print("Enter a valid number")


