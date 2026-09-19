print()
print("THIS DEVICE WILL ASSIGN YOU GRADES BASED ON YOUR MARKS")
print()
while True:
    try:
        marks = int(input("Please enter your marks:  "))
        print()
        if 101 > marks >= 90:
            print("You got an 'A'.")
            print()
            break
        elif 90 > marks >= 80:
            print("You got a 'B'.")
            print()
            break
        elif 80 > marks >= 70:
            print("You got a 'c'.")
            print()
            break
        elif 70 > marks >= 60:
            print("You got a 'D'.")
            print()
            break
        elif 60 > marks >= 50:
            print("You got an 'E'.")
            print()
            break
        elif 50 > marks >= 0:
            print("You got a 'F'.")
            print()
            break
        else:
            print("Marks should range from 0 to 100 !")
            print()
    except ValueError:
        print()
        print("Please enter valid marks !")
        print() 