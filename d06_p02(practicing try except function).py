while True:
    try:
        number = float(input("input a number"))
        print(f"You typed {number}")
        break

    except ValueError:
        print("Please enter a valid number")
