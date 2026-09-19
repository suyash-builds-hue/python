# Defining helper functions :--

def format_number(num):
        if num.is_integer():
            return int(num)
        return num

def add():     
    
    total = format_number(number1 + number2)
    print(f"{format_number(number1)} + {format_number(number2)} = {total}")

def subtract():
    
    minus = format_number(number1 - number2)
    print(f"{format_number(number1)} - {format_number(number2)} = {minus}")
            
def multiply():
    
    product = format_number(number1 * number2)
    print(f"{format_number(number1)} x {format_number(number2)} = {product}")


    while True:

        choice = input("To peform another calculation press 'y' otherwise to exit press 'n'").lower()

        if choice == "y":
            break

        elif choice == "n":
            exit()

        else:
            print("Please choose only 'y' or 'n'")

def restart():
    while True:
        choice = input("Choose 'y' for another calculation or choose 'n' to exit:  ")
        match choice:
            case "y":
                return True
            case "n":
                return False
            case _:
                print("Please choose from 'y' or 'n' !!")

# Calculator main body :--

while True:    
    try:
       
        print()
        number1 = float(input("Enter first number  "))
        print()
        number2 = float(input("Enter second number  "))
        print()
        operation = input("Please choose from: '+' '-' '*' '/' ").strip()
        print()

        match operation:
            case "+":
                add()
                print()
                if not restart():
                    print("Thank you for using our device")
                    break

            case "-":
                subtract()
                print()
                if not restart():
                    print("Thank you for using our device")
                    break

            case "*":
                multiply()
                print()
                if not restart():
                    print("Thank you for using our device")
                    break

            case "/":
                if number2 == 0:
                    print("Division by 0 is not possible, please enter valid values !! ")
                    print()
                else:
                    print(f"{format_number(number1)} ÷ {format_number(number2)} = {format_number(number1 / number2)}")
                    if not restart():
                        print("Thank you for using our device")
                        break

            case _:
                print("Invalid operation selected !!")
    
    except ValueError:
        print()
        print("Please enter valid values !!")