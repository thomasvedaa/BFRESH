
def modify_car_menu():
    while True:
        modify_car = int(input("1. Add car \n2. Edit car \n3. Remove car \n4. Exit"))
        if modify_car == 1:
            add_car_to_database(connection)
        elif modify_car == 2:
            pass
        elif modify_car == 3:
            pass
        elif modify_car==4:
            break
        else:
            print("Enter a valid number")