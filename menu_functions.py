from functions_customer import *
from functions_car import *
from functions_stats import *
from assign_function import *

db = 'rental_database.sqlite'



car_menu= Cars(db)
customer_menu = Customers(db)


def search_customer():
    while True:
        search_choice = int(input("1. Search for a customer \n2. Exit\n"))
        if search_choice == 1:
            pass
        elif search_choice == 2:
            break
        else:
            print("Enter a valid number")


def show_stats_menu():
    while True:
        stats_choice = int(input(
            "1. Number of customers \n2. Number of cars \n3. Number of active rentals \n4. Number of completed rentals \n5. Exit \n"))
        if stats_choice == 1:
            count_customers(connection)
        elif stats_choice == 2:
            count_cars(connection)
        elif stats_choice == 3:
            pass
        elif stats_choice == 4:
            pass
        elif stats_choice == 5:
            break
        else:
            print("Enter a valid number")
