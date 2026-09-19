print()
print("THIS DEVICE IS AN AGE CATEGORY CHECKER")
while True:
    try:
        print()
        age = int(input("Please enter your age in years:  "))
        print()
        if 0 < age < 13:
            print(f"The given age is of a {age}year old CHILD.")
            print()
            break
        elif 12 < age < 18:
            print(f"The given age is of a {age}year old TEENAGER.")
            print()
            break
        elif 17 < age < 35:
            print(f"The given age is of a {age}year old YOUNG ADULT.")
            print()
            break
        elif 34 < age < 55:
            print(f"The given age is of a {age}year old MIDDLE AGED ADULT.")
            print()
            break
        elif 54 < age < 65:
            print(f"The given age is of a {age}year old OLDER ADULT.")
            print()
            break 
        elif 64 < age:
            print(f"The given age is of a {age}year old SENIOR CITIZEN.")
            print()
            break
        else:
            print("Please enter a valid age !")    
    except ValueError:
        print("Please enter a valid age !")