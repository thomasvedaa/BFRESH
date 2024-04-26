import sqlite3
def add_car_to_database(connection):
    cursor = connection.cursor()
    print("Add a car")
    reg_nr=input("Enter registration number: ")
    state=input("Enter state of the car. From 1 to 10: ")
    price=input("Enter estimated price of the car (in USD): ")
    brand=input("Enter brand: ")
    cursor.execute('INSERT INTO Car (Registration_number,State,Price,Brand) VALUES (?,?,?,?)',(reg_nr,state,price,brand))
    connection.commit()
    car_id=cursor.lastrowid
    print(f'Added car: Id: {car_id}, registration number: {reg_nr}, price: {price}, brand: {brand}')


