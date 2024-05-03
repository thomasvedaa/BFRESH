import sqlite3

connection=sqlite3.connect('rental_database.sqlite')
cursor = connection.cursor()


def add_customer_to_database():
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
    customer_id = int(input("Which customer do you want to remove?"))
    cursor.execute('DELETE FROM Customer WHERE Customer_ID = ?', (customer_id,))
    connection.commit()
    if cursor.rowcount > 0:
        print(f'Customer with ID {customer_id} was removed')
    else:
        print('Customer not found')
