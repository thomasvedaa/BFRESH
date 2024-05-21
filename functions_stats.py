import sqlite3
from datetime import datetime


class Stats:

    def __init__(self,db):
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()
    def count_customers(self):
        self.cursor.execute('SELECT COUNT(Customer_ID) FROM Customer')
        customer_count=self.cursor.fetchone()
        print(f'There are {customer_count[0]} customers')

    def count_cars(self):
        self.cursor.execute('SELECT COUNT(Car_ID) FROM Car')
        car_count=self.cursor.fetchone()
        print(f'There are {car_count[0]} cars')

    def count_active_rentals(self):
        self.cursor.execute('SELECT COUNT(Rental_ID) FROM Active_rental')
        rental_count=self.cursor.fetchone()
        print(f'There are {rental_count[0]} active rentals')

    def count_completed_rentals(self):
        current_date = datetime.now().strftime('%Y-%m-%d')
        self.cursor.execute('SELECT COUNT(Rental_ID) FROM Active_rental WHERE End_date < ?', (current_date,))
        completed_rentals = self.cursor.fetchone()
        print(f'There are {completed_rentals[0]} completed rentals')
    def show_stats_menu(self):
        while True:
            stats_choice = int(input(
                "1. Number of customers \n2. Number of cars \n"
                "3. Number of active rentals \n4. Number of completed rentals \n5. Exit \n"))
            if stats_choice == 1:
                self.count_customers()
            elif stats_choice == 2:
                self.count_cars()
            elif stats_choice == 3:
                self.count_active_rentals()
            elif stats_choice == 4:
                self.count_completed_rentals()
            elif stats_choice == 5:
                break
            else:
                print("Enter a valid number")
