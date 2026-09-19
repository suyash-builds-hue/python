def modulus():
    print()
    print("Please enter an integral value for x.")
    while True:
        try:
            print()
            integer = int(input("What's x ?"))
            print()
            value = -integer
            if integer >= 0:
                print(f"The modulus of {integer} is {integer}.")
                print()
                break
            else:
                print(f"The modulus of {integer} is {value}.")
                print()
                break
        except ValueError:
            print("Please give an integral value !")
            print()

modulus()