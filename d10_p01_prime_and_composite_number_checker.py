# Prime or composite checker.

def restart():
    while True:
        choice = input("To use again press 'y' else to exit press 'n': ").strip().lower()
        match choice:
            case "y":
                print()
                return True
            case "n": 
                print()
                return False
            case _:
                print()
                print("Please choose from 'y' or 'n' !!")
                print()

def thank_you():
    print("Thank you for using our device.")
    print()

def prime():
    print()
    print("Given number is a prime number.")
    print()

def composite():
    print()
    print("Given number is a composite number.")
    print()

def neither(n):
    print()
    print(f"The number {n} is neither prime nor composite.")
    print()


print()
print("HI, THIS DEVICE CAN CHECK IF A NUMBER IS PRIME OR COMPOSITE")
print()

while True:
    
    try:
        
        number = int(input("What's the number: "))
        
        if number < 0:
            print()
            print("The number can't be negative !!")
            print("Please enter a natural number.")
            print()
        
        elif number in [0,1]:
            neither(number)
            if not restart():
                thank_you()
                break
        
        elif any(number % i == 0 for i in range(number - 1, 1, -1)):
            composite()
            if not restart():
                thank_you()
                break
        
        else:
            prime()
            if not restart():
                thank_you()
                break
    
    except ValueError:
        print()
        print("Please enter a natural number !!")
        print()