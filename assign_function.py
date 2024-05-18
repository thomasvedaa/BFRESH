import sqlite3
import datetime

class Assign_car:

    def __init__(self,db):
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()
    def assign_car_to_customer(self):

        #customer search
        customer_name_choice=input('Enter the name of the customer you want')
        self.cursor.execute('SELECT * FROM Customer WHERE Name LIKE ?', ('%'+customer_name_choice+'%',))
        customers=self.cursor.fetchall()
        if not customers:
            print("No customers")
            return

        for customer in customers:
            print(f'Found customer: Id: {customer[0]}, social security number: {customer[1]}, name: {customer[2]}, '
                  f'address: {customer[3]}, telephone number: {customer[4]}\n')


        #customer choice
        customer_choice = int(input('Enter ID of the customer you want: '))
        self.cursor.execute('SELECT * FROM Customer WHERE Customer_ID=?',(customer_choice,))
        chosen_customer=self.cursor.fetchone()
        customer_id=chosen_customer[0]


        #car search
        car_brand_choice=input('Enter the brand of the car you want')
        self.cursor.execute('SELECT * FROM Car WHERE Brand LIKE ?',('%'+car_brand_choice+'%',))
        cars=self.cursor.fetchall()
        if not cars:
            print('No cars')
            return

        for car in cars:
            print(
                f'Car: Id: {car[0]}, registration number: {car[1]}, state of car: {car[2]},  price: ${car[3]}, brand: {car[4]}')

        #car choice
        car_choice=int(input('Enter ID of the car you want'))
        self.cursor.execute('SELECT * FROM Car WHERE Car_ID=? ',(car_choice,))
        chosen_car=self.cursor.fetchone()
        car_id=chosen_car[0]



        #Calculate the start and end date
        #Used https://www.w3schools.com/python/python_datetime.asp for guidance on timedate
        days_of_rental=int(input('Enter how many days you would like to rent the car: '))
        start_date = datetime.datetime.now()
        end_date=start_date + datetime.timedelta(days=days_of_rental)

        start_date=start_date.strftime('%d-%m-%Y')
        end_date=end_date.strftime('%d-%m-%Y')


        self.cursor.execute('INSERT INTO Active_rental (Car_ID, Customer_ID, Start_date, End_date) VALUES(?,?,?,?)',(car_id,customer_id,start_date,end_date,))
        self.connection.commit()
        print('Rental successful')


    def unassign_car_to_customer(self):
        registration_number=input('Enter registration number of the car you want to unassign')
        current_date=datetime.datetime.now()
        self.cursor.execute('SELECT * FROM Active_rental, Car WHERE Car.Registration_number=? AND Car.Car_ID=Active_rental.Car_ID '
                            'AND Active_rental.End_date < ?',(registration_number,current_date,))
        active_rentals=self.cursor.fetchall()
        for rentals in active_rentals:
            print(f'Rental ID: {rentals[0]} Car ID:{rentals[1]} Customer ID: {rentals[2]} Start date: {rentals[3]} End date{rentals[4]}')

        unassign_car=int(input('Enter the Rental ID of the car you want to unassign'))
        self.cursor.execute('DELETE FROM Active_rental WHERE Rental_ID=')














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
