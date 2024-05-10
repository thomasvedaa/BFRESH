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
            print(f'Found customer: Id: {customer[0]}, social security number: {customer[1]}, name: {customer[2]}, address: {customer[3]}, telephone number: {customer[4]}\n')
            print('Select a car: ')
            self.cursor.execute('SELECT * FROM Car')
            cars=self.cursor.fetchall()
            for car in cars:
                print(f'Car: Id: {car[0]}, registration number: {car[1]}, state of car: {car[2]},  price: ${car[3]}, brand: {car[4]}')


        while True:
            car_choice=int(input("Which car do you want?\n"))
            if car_choice > car[0]:
                print("Enter a valid ID\n")
            else:
                self.cursor.execute('INSERT INTO Rental (Car_ID,Customer_ID) VALUES (?,?)',(car_choice,customer_id))
                self.connection.commit()
                print('Car successfully added')
                break







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
