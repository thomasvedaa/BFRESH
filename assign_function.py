import sqlite3

class Assign_car:

    def __init__(self,db):
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()
    def assign_car_to_customer(self):
        customer_name_choice=input('Enter the name of the customer you want')
        self.cursor.execute('SELECT * FROM Customer WHERE Name LIKE ?', ('%'+customer_name_choice+'%',))
        customers=self.cursor.fetchall()
        if not customers:
            print("No customers")
            return

        for customer in customers:
            print(f'Found customer: Id: {customer[0]}, social security number: {customer[1]}, name: {customer[2]}, '
                  f'address: {customer[3]}, telephone number: {customer[4]}\n')

        customer_choice = int(input('Enter ID of the customer you want: '))
        self.cursor.execute('SELECT * FROM Customer WHERE Customer_ID=?',(customer_choice,))
        chosen_customer=self.cursor.fetchone()
        customer_id=chosen_customer[0]

        car_brand_choice=input('Enter the brand of the car you want')
        self.cursor.execute('SELECT * FROM Car WHERE Brand LIKE ?',('%'+car_brand_choice+'%',))
        cars=self.cursor.fetchall()
        if not cars:
            print('No cars')
            return

        for car in cars:
            print(
                f'Car: Id: {car[0]}, registration number: {car[1]}, state of car: {car[2]},  price: ${car[3]}, brand: {car[4]}')

        car_choice=int(input('Enter ID of the car you want'))
        self.cursor.execute('SELECT * FROM Car WHERE Car_ID=? ',(car_choice,))
        chosen_car=self.cursor.fetchone()
        car=


    def unassign_car_to_customer(self):
        pass
    def assign_menu(self):
        while True:
            assign_choice = int(input("1. Assign car to customer\n2. Unassign car to customer \n3. Exit\n"))
            if assign_choice == 1:
                self.assign_car_to_customer()
            elif assign_choice == 2:
                self.unassign_car_to_customer()
            elif assign_choice == 3:
                break
            else:
                print("Enter a valid number")
