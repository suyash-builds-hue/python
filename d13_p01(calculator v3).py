# Defining helper functions for the calculator :--

def menu():
    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. View history")
    print("6. View error log")
    print("7. Exit\n")
    while True:
        try:
            choice = int(input("Please enter the number corresponding to the operation you want to perform: "))
            if choice in range(1, 8):
                if choice == 7:
                    print("\nExiting the calculator. Goodbye!\n")
                    exit()  
                return choice
            else:
                print("\nPlease enter a valid number between 1 and 7 !!\n")
        except ValueError:
            error_log.append("Invalid menu selection")
            print("\nPlease enter a valid number !!\n")

def format_number(num):
        if num.is_integer():
            return int(num)
        return num

def add():         
    total = format_number(number1 + number2)
    statement = (f"{format_number(number1)} + {format_number(number2)} = {total}")
    return statement

def subtract():    
    minus = format_number(number1 - number2)
    statement = (f"{format_number(number1)} - {format_number(number2)} = {minus}")
    return statement

def multiply():
    product = format_number(number1 * number2)
    statement = (f"{format_number(number1)} x {format_number(number2)} = {product}")
    return statement

def divide():
        quotient = format_number(number1 / number2)
        statement = (f"{format_number(number1)} ÷ {format_number(number2)} = {quotient}")
        return statement

def zero_division_handler():
    while True:
        way = input("To re-select second number, enter 'R' otherwise to go to menu enter 'M' :  ").upper().strip()
        match way:
            case "R":
                return False
            case "M":
                return True
            case _:
                error_log.append("Invalid response after division by zero")
                print("\nPlease choose from 'R' or 'M' !!\n")

def reselect_denominator():
    while True:
        try:
            number2 = float(input("\nEnter second number:  "))
            if number2 != 0:
                return number2
            else:
                print("\nSecond number cannot be zero for division !!\n")
                if not zero_division_handler():
                    continue
                else:
                    return None
        except ValueError:
            error_log.append("Invalid input for re-selection of second number")
            print("\nPlease enter a valid number !!\n")

def data_menu_handler(p):
    name = "History" if p == history else "Error log"
    while True:
        print(f"\n1. To clear {name}, enter 'C'")
        print("2. To go to menu, enter 'M'")
        print("3. To exit, enter 'E'")
        way = input("\n").upper().strip()
        match way:
            case "C":
                p.clear()
                print(f"\n{name} cleared successfully !!")
                break
            case "M":
                break
            case "E":
                print("\nExiting the calculator. Goodbye!\n")
                exit()
            case _:
                error_log.append("Invalid response in error/history menu")
                print("\nPlease choose from 'C','M' or 'E' !!\n")

def view_history():
    if history:
        print("\nHistory of calculations:")
        for record in history:
            print(record)
        data_menu_handler(history)
    else:
        print("\nNo calculations performed yet.")

def view_error_log():
    if error_log:
        print("\nError log:")
        for error in error_log:
            print(error)
        data_menu_handler(error_log)
    else:
        print("\nNo errors logged yet !!")

history = []  # List to store history of calculations

error_log = []  # List to store error messages

# Main body of the calculator :--

print("\n-----------Calculator-----------\n")
choice = menu()
while True:
    
    if choice in range(1, 5):
        try:
            number1 = float(input("\nEnter first number:  "))
            number2 = float(input("\nEnter second number:  "))
            match choice:
                
                case 1:
                    statement = add()
                    print(f"\n{statement}")
                    history.append(statement)

                case 2:
                    statement = subtract()
                    print(f"\n{statement}")
                    history.append(statement)
                case 3:
                    statement = multiply()
                    print(f"\n{statement}")
                    history.append(statement)

                case 4:
                    
                    if number2 != 0:
                        statement = divide()
                        print(f"\n{statement}")
                        history.append(statement)
                    else:
                        error_log.append("Attempted division by zero")
                        print("\nDivision by zero is not possible !!\n")
                        if not zero_division_handler():
                            number2 = reselect_denominator()
                            if number2 is None:
                                continue
                            else:
                                statement = divide()
                                print(f"\n{statement}")
                                history.append(statement)

        except ValueError:
            error_log.append("Invalid number entered")
            print("\nPlease enter valid numbers !!\n")
            continue

    else:
        match choice:
            case 5:
                view_history()

            case 6:
                view_error_log()
    
    choice = menu()