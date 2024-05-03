import sqlite3

connection=sqlite3.connect('rental_database.sqlite')
cursor = connection.cursor()


def add_customer_to_database():
    print("Add a customer")
    social_security_number = input("Enter social security number: ")
    name = input("Enter customer name: ")
    adress = input("Enter customer address: ")
    telephone_number = int(input("Enter phone number: "))
    cursor.execute('INSERT INTO Customer (Social_security_number,Name,Adress,Telephone_number) VALUES (?,?,?,?)',(social_security_number, name, adress, telephone_number))
    connection.commit()
    customer_id=cursor.lastrowid
    print(f'Added customer: Id: {customer_id}, name: {name}, adress: {adress}, phone number: {telephone_number}\n')

def edit_customer():
    customer_id = int(input("Enter customer to edit: "))
    cursor.execute('SELECT * FROM Customer WHERE Customer_ID = ?', (customer_id,))
    customer = cursor.fetchone()
    if customer is None:
        print("No customer with that ID")
        return
    else:
        print(
            f'Found customer: Id: {customer[0]}, social security number: {customer[1]}, name: {customer[2]}, address: {customer[3]}, telephone number: {customer[4]}\n')
        social_number = input("Update social security number: ")
        name = input("Update name: ")
        adress = input("Update address: ")
        phone_number = input("Update phone number: ")
        cursor.execute('UPDATE Customer SET Social_security_number = ?, Name = ?, Adress = ?, Telephone_number = ? WHERE Customer_ID = ?',
                       (social_number, name, adress, phone_number, customer_id,))
        connection.commit()
        print(
            f'Updated customer: Id: {customer_id}, name: {name}, social security number: {social_number}, address: {adress}, telephone number: {phone_number}')

def remove_customer():
    customer_id = int(input("Which customer do you want to remove?\n"))
    cursor.execute('DELETE FROM Customer WHERE Customer_ID = ?', (customer_id,))
    connection.commit()
    if cursor.rowcount > 0:
        print(f'Customer with ID {customer_id} was removed\n')
    else:
        print('Customer not found\n')
