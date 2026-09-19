# Defining some fully autonomous functions :--

"""Please note that some local helper functions are repeated in all these functions
   this is done in order to remove and kind of dependency and make each defined 
   function able to work fully independent on their own."""

def add():
    
    def format_number(num):
        if num.is_integer():
            return int(num)
        return num
       
    while True:
        try:
            
            print()
            number1=float(input("Enter first number  "))
            print()
            number2=float(input("Enter second number  "))
            print()

            total = format_number(number1 + number2)
            
            print(f"{format_number(number1)} + {format_number(number2)} = {total}")
            print()
            break
        
        except ValueError:
            print()
            print("Please enter valid values !!")

def subtract():
    
    def format_number(num):
        if num.is_integer():
            return int(num)
        return num
       
    while True:
        try:
            
            print()
            number1=float(input("Enter first number  "))
            print()
            number2=float(input("Enter second number  "))
            print()

            minus = format_number(number1 - number2)
            
            print(f"{format_number(number1)} - {format_number(number2)} = {minus}")
            print()
            break
        
        except ValueError:
            print()
            print("Please enter valid values !!")

def multiply():
    
    def format_number(num):
        if num.is_integer():
            return int(num)
        return num
       
    while True:
        try:
            
            print()
            number1=float(input("Enter first number  "))
            print()
            number2=float(input("Enter second number  "))
            print()

            product = format_number(number1 * number2)
            
            print(f"{format_number(number1)} x {format_number(number2)} = {product}")
            print()
            break
        
        except ValueError:
            print()
            print("Please enter valid values !!")

def division():
    
    def format_number(num):
        if num.is_integer():
            return int(num)
        return num
    
    while True:
        try:
            print()
            number1=float(input("Enter first number  "))
            print()
            
            while True:
                try:    
                    print()
                    number2=float(input("Enter second number  "))
                    print()
                    if number2 == 0:
                        print("Division by 0 is not possible, \nplease enter a valid number !! ")
                        print()
                    else:
                        quotient = number1 / number2

                        print(f"{format_number(number1)} ÷ {format_number(number2)} = {format_number(quotient)}")
                        print()
                        break
                
                except ValueError:
                    print()
                    print("Please enter valid values !!")
            break

        except ValueError:
            print()
            print("Please enter valid values !!")        