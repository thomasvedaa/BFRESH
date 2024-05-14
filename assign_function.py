import sqlite3

class Assign_car:

    def __init__(self,db):
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()
    def assign_car_to_customer(self):
        customer_ssn=int(input('Enter social security number to identify yourself: '))
        self.cursor.execute('SELECT * FROM Customer WHERE Social_security_number=?', (customer_ssn,))
        customer=self.cursor.fetchone()
        customer_id=customer[0]
        if customer is None:
            print("No customer with that social security number")

        else:
            print(f'Found customer: Id: {customer[0]}, social security number: {customer[1]}, name: {customer[2]}, '
                  f'address: {customer[3]}, telephone number: {customer[4]}\n')
            print('Select a car: ')
            self.cursor.execute('SELECT * FROM Car')
            cars=self.cursor.fetchall()
            if not cars:
                print('No cars available')
            for car in cars:
                print(f'Car: Id: {car[0]}, registration number: {car[1]}, state of car: {car[2]},  price: ${car[3]}, brand: {car[4]}')


        while True:
            car_choice=int(input("Which car do you want?\n"))
            Start_date=input('Enter start date: ')
            End_date=input('Enter end date: ')
            self.cursor.execute('SELECT * FROM Car')
            car=self.cursor.fetchone()
            if car_choice > car[0]:
                print("Enter a valid ID\n")
            else:
                start_date=input('Enter start date of rental in DD.MM.YYYY')
                end_date=input('Enter end date of rental in DD.MM.YYYY')
                self.cursor.execute('INSERT INTO Active_rental (Car_ID,Customer_ID,Start_date, End_date) VALUES (?,?,?,?)',(car_choice,customer_id,start_date,end_date))
                self.connection.commit()
                print('Car successfully assigned')
                break







    def unassign_car_to_customer(self):
        customer_ssn = int(input('Enter social security number to identify yourself: '))
        self.cursor.execute('SELECT * FROM Customer WHERE Social_security_number=?', (customer_ssn,))
        customer = self.cursor.fetchone()
        customer_id = customer[0]
        if customer is None:
            print("No customer with that social security number")

        else:
            print(f'Found customer: Id: {customer[0]}, social security number: {customer[1]}, name: {customer[2]}, '
                  f'address: {customer[3]}, telephone number: {customer[4]}\n')
            print('Select a car: ')
            self.cursor.execute('SELECT * FROM Car')
            cars = self.cursor.fetchall()
            if not cars:
                print('No cars available')
            for car in cars:
                print(
                    f'Car: Id: {car[0]}, registration number: {car[1]}, state of car: {car[2]},  price: ${car[3]}, '
                    f'brand: {car[4]}')

        while True:
            car_choice = int(input("Which car do you want to unassign?\n"))
            if car_choice > car[0]:
                print("Enter a valid ID\n")
            else:
                self.cursor.execute('DELETE FROM Active_rental WHERE Car_ID=? AND Customer_ID=?', (car_choice, customer_id))
                self.connection.commit()
                print('Car successfully unassigned')
                break





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
