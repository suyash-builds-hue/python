# TITLE :
print()
print("THIS DEVICE CAN CHECK IF A VALUE IS A ROOT OF A QUADRATIC OR NOT")
print()
print("! Please note that this device can only check for quadratic equation.")
print()   

# Figuring out the quadratic:
print("The quadratic is ax² + bx + c")
print()
while True:   
    try:    
        a = float(input("The value of 'a' is:  "))
        print()
        b = float(input("The value of 'b' is:  "))
        print()
        c = float(input("The value of 'c' is:  "))
        print()
        if a != 0:
            print(f"The given polynomial is {a}x² + {b}x + {c}")
            print()    
            # Determining type of roots:
            while True:
                rootType = input("For simple roots press 'S' otherwise for surd roots press 'T':  ").upper().strip()
                print()
                match rootType:
                    case "S" | "T":
                        match rootType:
                            # If roots are simple:
                            case "S":
                                while True:
                                    quantity = input("To check one root press '1' otherwise to check both roots press '2':  ").strip()
                                    match quantity:
                                        case "2":
                                            while True:
                                                try:
                                                    print()
                                                    simpleR1 = float(input("Please give first root: "))
                                                    print()
                                                    simpleR2 = float(input("Please give second root: "))
                                                    print()
                                                    value1 = a*(simpleR1**2) + b*simpleR1 + c
                                                    value2 = a*(simpleR2**2) + b*simpleR2 + c
                                                    if abs(value1) < 0.000001 and abs(value2) < 0.000001:
                                                        print(f"Both {simpleR1} and {simpleR2} are roots of the polynomial {a}x² + {b}x + {c}")
                                                        print()
                                                        print("Thank you for using our device.")
                                                        print()
                                                        break
                                                    elif abs(value1) >= 0.000001 and abs(value2) < 0.000001:
                                                        print(f"Only {simpleR2} is root of the polynomial {a}x² + {b}x + {c}")
                                                        print()
                                                        print(f"The value of {a}x² + {b}x + {c} at x = {simpleR1} is {value1}")
                                                        print()
                                                        print("Thank you for using our device.")
                                                        print()
                                                        break
                                                    elif abs(value1) < 0.000001 and abs(value2) >= 0.000001:
                                                        print(f"Only {simpleR1} is the root of the polynomial {a}x² + {b}x + {c}")
                                                        print()
                                                        print(f"The value of {a}x² + {b}x + {c} at x = {simpleR2} is {value2}")
                                                        print()
                                                        print("Thank you for using our device.")
                                                        print()
                                                        break
                                                    else:
                                                        print(f"Both {simpleR1} and {simpleR2} are not the roots of the polynomial {a}x² + {b}x + {c}")
                                                        print()
                                                        print(f"The value of {a}x² + {b}x + {c} at x = {simpleR1} is {value1}")
                                                        print()
                                                        print(f"The value of {a}x² + {b}x + {c} at x = {simpleR2} is {value2}")
                                                        print()
                                                        print("Thank you for using our device.")
                                                        print()
                                                        break
                                                except ValueError:
                                                    print("Please enter valid roots !")
                                                    print()
                                            break        
                                        case "1":
                                            while True:
                                                try:
                                                    print()
                                                    simpleR01 = float(input("Please give in the root: "))
                                                    print()
                                                    value01 = a*(simpleR01**2) + b*simpleR01 + c
                                                    if abs(value01) < 0.000001:
                                                        print(f"{simpleR01} is root of the polynomial {a}x² + {b}x + {c}")
                                                        print()
                                                        print("Thank you for using our device.")
                                                        print()
                                                        break
                                                    else:
                                                        print(f"{simpleR01} is not the root of the polynomial {a}x² + {b}x + {c}")
                                                        print()
                                                        print(f"The value of {a}x² + {b}x + {c} at x = {simpleR01} is {value01}")
                                                        print()
                                                        print("Thank you for using our device.")
                                                        print()
                                                        break
                                                except ValueError:
                                                    print("Please give a valid root !")
                                                    print()
                                            break        
                                        case _:
                                            print("Please choose from 1 and 2 !")
                                break              
                        # If roots are surd:
                            case _:
                                print("Your roots are in the form of (A ± √D) / C")
                                while True:
                                    try:
                                        numerator = float(input("What is the value of 'A':  "))
                                        print()
                                        discriminant = float(input("What is the value of 'D':  "))
                                        print()
                                        denominator = float(input("What is the value of 'C':  "))
                                        print()
                                        if discriminant >= 0 and denominator != 0:
                                            surdR1 = (numerator+(discriminant)**(1/2))/denominator
                                            surdR2 = (numerator-(discriminant)**(1/2))/denominator
                                            print(f"Given roots are ({numerator} + √{discriminant})/{denominator} and ({numerator} - √{discriminant})/{denominator}")
                                            print()
                                            value3 = a*(surdR1**2) + b*surdR1 + c
                                            value4 = a*(surdR2**2) + b*surdR2 + c
                                            if abs(value3) < 0.000001 and abs(value4) < 0.000001:
                                                print(f"Both ({numerator} + √{discriminant})/{denominator} and ({numerator} - √{discriminant})/{denominator} are roots of the polynomial {a}x² + {b}x + {c}")
                                                print()
                                                print("Thank you for using our device.")
                                                print()
                                                break
                                            else:
                                                print(f"Both ({numerator} + √{discriminant})/{denominator} and ({numerator} - √{discriminant})/{denominator} are not the roots of {a}x² + {b}x + {c}")
                                                print()
                                                print(f"The value of {a}x² + {b}x + {c} at x = ({numerator} + √{discriminant})/{denominator} is {value3}.")
                                                print()
                                                print(f"The value of {a}x² + {b}x + {c} at x = ({numerator} - √{discriminant})/{denominator} is {value4}.")
                                                print()
                                                print("Thank you for using our device.")
                                                print()
                                                break
                                        elif denominator == 0:
                                            print("The value of 'C' can't be 0 !")
                                        else:
                                            print("Value of 'D' can't be negative !")
                                    except ValueError:
                                        print("Please enter valid values of A, C and D !")
                                        print()
                                break        
                    case _:
                        print("Please choose from 'S' and 'T' !")
                        print()
            break
        else:
            print("For quadratic the value of 'a' can't be 0 !")
            print()        
    except ValueError:
        print("Please give valid values of a, b and c !")
        print()