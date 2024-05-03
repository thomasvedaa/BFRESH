import sqlite3

connection = sqlite3.connect('rental_database.sqlite')
cursor = connection.cursor()


def add_car_to_database():
    print("Add a car")
    reg_nr = input("Enter registration number: ")
    state = input("Enter state of the car. From 1 to 10: ")
    price = input("Enter estimated price of the car (in USD): ")
    brand = input("Enter brand: ")
    cursor.execute('INSERT INTO Car (Registration_number,State,Price_range,Brand) VALUES (?,?,?,?)',
                   (reg_nr, state, price, brand))
    connection.commit()
    car_id = cursor.lastrowid
    print(f'Added car: Id: {car_id}, registration number: {reg_nr}, price: {price}, brand: {brand}')


def edit_car():
    car_id = int(input("Give a valid Car ID to search after: "))
    cursor.execute('SELECT * FROM Car WHERE Car_ID = ?', (car_id,))
    car = cursor.fetchone()
    if car is None:
        print("No car with that ID")
        return
    else:
        print(
            f'Found car: Id: {car[0]}, registration number: {car[1]}, state of car: {car[2]},  price: ${car[3]}, brand: {car[4]}')
        reg_nr = input("Update registration number: ")
        state = input("Update state of the car. From 1 to 10: ")
        price = input("Update estimated price of the car (in USD): ")
        brand = input("Update brand: ")
        cursor.execute('UPDATE Car SET Registration_number = ?, State = ?, Price_range = ?, Brand = ? WHERE Car_ID = ?',
                       (reg_nr, state, price, brand,car_id,))
        connection.commit()
        print(
            f'Updated car: Id: {car_id},state of car: {state} registration number: {reg_nr}, price: {price}, brand: {brand}')


def remove_car():
    car_id = int(input("Which car do you want to remove?"))
    cursor.execute('DELETE FROM Customer WHERE Customer_ID = ?', (car_id,))
    connection.commit()
    if cursor.rowcount > 0:
        print(f'Car with ID {car_id} was removed')
    else:
        print('Car not found')
