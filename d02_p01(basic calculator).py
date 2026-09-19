print()
print("THIS IS A VERY BASIC CALCULATOR FOR 2 NUMBERS ONLY")
# Taking input
print()
a=float(input("Enter first number  "))
print()
b=float(input("Enter second number  "))
print()

while True: 

      c=input("Please input the operation you want to peform (+, -, *, /):  ")
      print()
      
# If addition requested 
      if c == "+":
        print("The sum of the 2 numbers is", a+b)
        print()
        break
# If subtraction is requested
      elif c == "-":
        print(f"The subtraction of {b} from {a} gives", a-b)
        break
# If multiplication is requested
      elif c == "*":
        print(f"The product of {a} and {b} is", a*b)
        print()
        break
# If division is requested
      elif c == "/":
          if b == 0:
             print("Division with zero is not possible, please enter a non-zero number or change you operation ")
             print()
             b=float(input("Please enter a non-zero number:  "))
             print()
             if b == 0:
                while True:
                      c=input("Please select an operation other than division (+, -, *):  ")
                      print()
                      if c == "+":
                         print("The sum of the 2 numbers is", a+b)
                         print()
                         break
                      elif c == "-":
                         print(f"The subtraction of {b} from {a} gives", a-b)
                         print()
                         break
                      elif c == "*":
                         print(f"The product of {a} and {b} is", a*b)
                         print()
                         break
                      else:
                         print("Invalid operation selected")
                         print()
                break
             else:
                print(f"The division of {a} by {b} gives", a/b)
                print()
                break     
          else:
             print(f"The division of {a} by {b} gives", a/b)
             print()
             break
      else:
        print("Invalid operation selected")
        print()
        c=input("Please select a valid operation (+, -, *, /):  ")
        print()
   
