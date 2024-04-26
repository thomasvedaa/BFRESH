import sqlite3
def add_customer_to_database(connection):
    cursor = connection.cursor()
    print("Add a customer")
    social_security_number = input("Enter social security number: ")
    name = input("Enter customer name: ")
    adress = input("Enter customer adress: ")
    telephone_number = int(input("Enter phone number: "))
    cursor.execute('INSERT INTO Customer (Social_security_number,Name,Adress,Telephone_number) VALUES (?,?,?,?)',(social_security_number, name, adress, telephone_number))
    connection.commit()
    customer_id=cursor.lastrowid
    print(f'Added customer: Id: {customer_id}, name: {name}, adress: {adress}, phone number: {telephone_number}')

def edit_customer():
    pass


def remove_customer():
    pass
