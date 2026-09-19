#Title
print()
print("THIS DEVICE WILL CHECK IF A NUMBER IS DIVISIBLE BY THE OTHER OR NOT")
print()
# Input
a=int(input("Please enter the number to be checked for division  "))
print()
b=int(input("Please enter the number which will divide  "))
print()
#Checking for b=0
while True:
    if b == 0:
             print("! Division by 0 is not possible")
             print()
             b=int(input("Please enter a number other than 0: "))
    else:
        if a%b == 0:
            print()
            print(f"The number {a} is completely divisible by {b}")
            print("Quotient =", a//b)
            print("Remainder =", a%b)
            print()
            break
        else:
            print(f"The number {a} is partially divisible by {b}")
            print("Quotient =", a//b)
            print("Remainder =", a%b)
            break
print()
print("Thank you for using our device.")
print()                
