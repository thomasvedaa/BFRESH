import sqlite3


def count_customers(connection):
    cursor = connection.cursor()
    cursor.execute('SELECT COUNT(Customer_ID) FROM Customer')
    customer_count=cursor.fetchall()
    print(f'There are {customer_count[0][0]} customers')

def count_cars(connection):
    cursor = connection.cursor()
    cursor.execute('SELECT COUNT(Customer_ID) FROM Customer')
    car_count=cursor.fetchall()
    print(f'There are {car_count[0][0]} cars')
