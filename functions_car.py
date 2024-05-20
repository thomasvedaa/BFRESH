import sqlite3

connection = sqlite3.connect('rental_database.sqlite')
cursor = connection.cursor()


class Cars:
    def __init__(self, db):
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()

    def add_car_to_database(self):
        print("Add a car")
        reg_nr = input("Enter registration number: ")
        brand = input("Enter brand of the car: ")
        model = input("Enter model of the car: ")
        price = input("Enter estimated price of the car (in USD): ")
        self.cursor.execute('INSERT INTO Car (Registration_number,Brand,Model,Price) VALUES (?,?,?,?)',
                            (reg_nr, brand, model, price))
        self.connection.commit()
        car_id = self.cursor.lastrowid
        print(f'Added car: Id: {car_id}, registration number: {reg_nr}, brand: {brand}, model: {model}, price: ${price}\n')

    def edit_car(self):
        car_id = int(input("Give a valid Car ID to search after: "))
        self.cursor.execute('SELECT * FROM Car WHERE Car_ID = ?', (car_id,))
        car = self.cursor.fetchone()
        if car is None:
            print("No car with that ID")
            return
        else:
            print(
                f'Found car: Id: {car[0]}, registration number: {car[1]},brand: {car[2]},  model: {car[3]}, price: ${car[4]}')
            reg_nr = input("Update registration number: ")
            brand = input("Update brand of the car:")
            model = input("Update model of the car: ")
            price = input("Update estimated price of the car (in USD): ")
            self.cursor.execute(
                'UPDATE Car SET Registration_number = ?, Brand = ?, Model = ?, Price = ? WHERE Car_ID = ?',
                (reg_nr, brand, model, price, car_id,))
            self.connection.commit()
            print(
                f'Updated car: Id: {car_id},state of car: {brand} registration number: {reg_nr}, model: {model}, brand: {price}\n')

    def remove_car(self):
        car_id = int(input("Which car do you want to remove?\n"))
        self.cursor.execute('DELETE FROM Car WHERE Car_ID = ?', (car_id,))
        self.connection.commit()
        if self.cursor.rowcount > 0:
            print(f'Car with ID {car_id} was removed\n')
        else:
            print('Car not found\n')

    def modify_car_menu(self):
        while True:
            modify_car = int(input("1. Add car \n2. Edit car \n3. Remove car \n4. Exit\n"))
            if modify_car == 1:
                self.add_car_to_database()
            elif modify_car == 2:
                self.edit_car()
            elif modify_car == 3:
                self.remove_car()
            elif modify_car == 4:
                break
            else:
                print("Enter a valid number")
