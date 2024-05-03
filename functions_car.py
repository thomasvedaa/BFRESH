import sqlite3
def add_car_to_database(connection):
    cursor = connection.cursor()
    print("Add a car")
    reg_nr=input("Enter registration number: ")
    state=input("Enter state of the car. From 1 to 10: ")
    price=input("Enter estimated price of the car (in USD): ")
    brand=input("Enter brand: ")
    cursor.execute('INSERT INTO Car (Registration_number,State,Price_range,Brand) VALUES (?,?,?,?)',(reg_nr,state,price,brand))
    connection.commit()
    car_id=cursor.lastrowid
    print(f'Added car: Id: {car_id}, registration number: {reg_nr}, price: {price}, brand: {brand}')


def edit_car():
    cursor = connection.cursor()
    car_id = int(input("Give a valid Car ID to search after: "))
    cursor.execute('SELECT * FROM Car WHERE Car_ID = ?', (ID,))
    car = cursor.fetchone()
    if car is None:
        print("No car with that ID")
        return
    else:
        print(f'Found car: Id: {car[0]}, state of car: {car[2]}, registration number: {car[1]}, price: {car[3]}, brand: {car[4]}')
        reg_nr = input("Update registration number: ")
        state = input("Update state of the car. From 1 to 10: ")
        price = input("Update estimated price of the car (in USD): ")
        brand = input("Update brand: ")
        cursor.execute('UPDATE Car SET Registration_number = ?, State = ?, Price = ?, Brand = ?',
                       (reg_nr, state, price, brand))
        connection.commit()
        car_id = ID
        print(f'Updated car: Id: {car_id},state of car: {state} registration number: {reg_nr}, price: {price}, brand: {brand}')


def remove_car():
    pass
