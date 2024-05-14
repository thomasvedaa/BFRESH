import sqlite3

class Stats:

    def __init__(self,db):
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()
    def count_customers(self):
        self.cursor.execute('SELECT COUNT(Customer_ID) FROM Customer')
        customer_count=self.cursor.fetchall()
        print(f'There are {customer_count[0][0]} customers')

    def count_cars(self):
        self.cursor.execute('SELECT COUNT(Car_ID) FROM Car')
        car_count=self.cursor.fetchall()
        print(f'There are {car_count[0][0]} cars')

    def count_active_rentals(self):
        self.cursor.execute('SELECT COUNT(Rental_ID) FROM Active_rental')
        rental_count=self.cursor.fetchall()
        print(f'There are {rental_count[0][0]} active rentals')
    def show_stats_menu(self):
        while True:
            stats_choice = int(input(
                "1. Number of customers \n2. Number of cars \n3. Number of active rentals \n4. Number of completed rentals \n5. Exit \n"))
            if stats_choice == 1:
                self.count_customers()
            elif stats_choice == 2:
                self.count_cars()
            elif stats_choice == 3:
                self.count_active_rentals()
            elif stats_choice == 4:
                pass
            elif stats_choice == 5:
                break
            else:
                print("Enter a valid number")
