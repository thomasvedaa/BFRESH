import sqlite3
import csv


class Csv_database:
    def __init__(self, db):
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()

    def write_to_csv(self, table):
        self.table = table
        self.cursor.execute(f'SELECT * FROM {self.table}')
        data = self.cursor.fetchall()

        columns = [column[0] for column in self.cursor.description]

        with open(f'{self.table}.csv', 'w', newline='') as csv_table:
            csvwriter = csv.writer(csv_table)

            csvwriter.writerow(columns)
            csvwriter.writerows(data)

        print(f'{self.table}.csv created successfully, information exported!')

    def choose_export(self):
        while True:
            export_choice = int(input('Choose which table to export.\n'
                                      '1. Customer\n'
                                      '2. Car\n'
                                      '3. Rental\n'))
            if export_choice == 1:
                self.table = 'Customer'
                self.write_to_csv(self.table)
                return
            elif export_choice == 2:
                self.table = 'Car'
                self.write_to_csv(self.table)
                return
            elif export_choice == 3:
                self.table = 'Active_rental'
                self.write_to_csv(self.table)
                return
            else:
                print('Enter valid number')

    def write_to_database(self, table):

        self.table = table
        with open(f'{self.table}.csv', 'r', newline='') as csv_file:
            reader = csv.reader(csv_file)
            data = list(reader)


            # used https://stackoverflow.com/a/21261532/25128641 to solve the problem, needed the headers
            # to become columns in the database
            columns = data[0]
            values = ','.join('?'*len(columns))
            column_names = ','.join(columns)

            for x in data[1:]:
                insert = f'INSERT INTO {self.table}({column_names}) VALUES({values})'
                self.cursor.execute(insert, x)
                self.connection.commit()
            print("Application committed successfully, imported information to database")

    def choose_import(self):

        while True:
            import_choice = int(input('Choose which csv file to import.\n'
                                      '1. Customer\n'
                                      '2. Car\n'
                                      '3. Rental\n'))
            if import_choice == 1:
                self.table = 'Customer'
                self.write_to_database(self.table)
                return
            elif import_choice == 2:
                self.table = 'Car'
                self.write_to_database(self.table)
                return
            elif import_choice == 3:
                self.table = 'Active_rental'
                self.write_to_database(self.table)
                return
            else:
                print('Enter valid number')
