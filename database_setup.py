import sqlite3

class Database_setup:
    def __init__(self, db):
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()

    def create_database(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Customer
            (
                Customer_ID            INTEGER PRIMARY KEY AUTOINCREMENT,
                Social_security_number INTEGER NOT NULL UNIQUE,
                Name                   TEXT,
                Adress                 TEXT,
                Telephone_number       INTEGER
            );
        ''')
        self.connection.commit()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Car
            (
                Car_ID              INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                Registration_number TEXT UNIQUE,
                Brand               TEXT,
                Model               TEXT,
                Price               INTEGER
            );
        ''')
        self.connection.commit()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Active_rental
            (
                Rental_ID   INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                Car_ID      INTEGER,
                Customer_ID INTEGER,
                Start_date  INTEGER,
                End_date    INTEGER,
                FOREIGN KEY (Car_ID) REFERENCES Car(Car_ID),
                FOREIGN KEY (Customer_ID) REFERENCES Customer(Customer_ID)
            );
        ''')
        self.connection.commit()
