from functions_customer import *
from functions_car import *
from functions_stats import *
from assign_function import *

db = 'rental_database.sqlite'



car_menu= Cars(db)
customer_menu = Customers(db)
stats=Stats(db)


def search_customer():
    while True:
        search_choice = int(input("1. Search for a customer \n2. Exit\n"))
        if search_choice == 1:
            pass
        elif search_choice == 2:
            break
        else:
            print("Enter a valid number")


