import random

def rules():
    
    print("""
Game rules:
 1. First you will have to choose your desired level.
 2. The system wil select a random number.
 3. You will have to guess the number with the help of the hints provided.
 4. Be careful, you will only get a limited number of tries !""")

levels = {
        1 : {"Name": "Practice", "tries": "unlimited", "max": 10},
        2 : {"Name": "Easy", "tries": 10, "max": 25},
        3 : {"Name": "Medium", "tries": 8, "max": 50},
        4 : {"Name": "Hard", "tries": 7, "max": 75},
        5 : {"Name": "Impossible", "tries": 6, "max": 100}}

def level():
    
    print("""\nPlease choose the difficulty level:
 1. Practice
 2. Easy
 3. Medium
 4. Hard
 5. Impossible
""")
    
    while True:
        
        try:
            
            desire = int(input("Enter the number corresponding to your desired level:  "))
            
            if desire in levels:
                
                print(f"\nYou have choosen {levels[desire]['Name']}.\n")
                
                print(f"You will get {levels[desire]['tries']} tries for this level.\n")
                
                print(f"The secret number can be anywhere from 1 to {levels[desire]['max']}.\n")
                return desire
            
            else:
                
                print("\nPlease choose a valid level !\n")
                
        except ValueError:
            
            print("\nPlease select from the numbers corresponding to the levels !\n")
            
def re_level(current_level):
    
    while True:
        
        print("""To continue press 'C'
to reselect the level press 'R',
otherwise press 'E' to exit the game.\n""")
        
        select = input().strip().upper()
        
        match select:
            
            case "C":
                return current_level
           
            case "E":
                print()
                exit()
            
            case "R":
                current_level = level()
            
            case _:
                print("Please choose a valid input !")

def compare(distance, level):

    if level == 1:

        if distance == 1:
            print("\nYou are extremely close !\n")
        elif distance == 2:
            print("\nYou are very close !\n")
        elif distance == 3:
            print("\nYou are close !\n")
        elif distance == 4:
            print("\nNot too far !\n")
        elif 4 < distance < 7:
            print("\nYou are far away !\n")
        elif 6 < distance < 9:
            print("\nYou are very far away !\n")
        else:
            print("\nNowhere near it !\n")

    elif level == 2:

        if 0 < distance < 3:
            print("\nYou are extremely close !\n")
        elif 2 < distance < 5:
            print("\nYou are very close !\n")
        elif 4 < distance < 8:
            print("\nYou are close !\n")
        elif 7 < distance < 11:
            print("\nNot too far !\n")
        elif 10 < distance < 16:
            print("\nYou are far away !\n")
        elif 15 < distance < 21:
            print("\nYou are very far away !\n")
        else:
            print("\nNowhere near it !\n")

    elif level == 3:

        if 0 < distance < 4:
            print("\nYou are extremely close !\n")
        elif 3 < distance < 7:
            print("\nYou are very close !\n")
        elif 6 < distance < 13:
            print("\nYou are close !\n")
        elif 12 < distance < 19:
            print("\nNot too far !\n")
        elif 18 < distance < 26:
            print("\nYou are far away !\n")
        elif 25 < distance < 36:
            print("\nYou are very far away !\n")
        else:
            print("\nNowhere near it !\n")

    elif level == 4:

        if 0 < distance < 5:
            print("\nYou are extremely close !\n")
        elif 4 < distance < 9:
            print("\nYou are very close !\n")
        elif 8 < distance < 16:
            print("\nYou are close !\n")
        elif 15 < distance < 26:
            print("\nNot too far !\n")
        elif 25 < distance < 41:
            print("\nYou are far away !\n")
        elif 40 < distance < 56:
            print("\nYou are very far away !\n")
        else:
            print("\nNowhere near it !\n")

    elif level == 5:
        if 0 < distance < 6:
            print("\nYou are extremely close !\n")
        elif 5 < distance < 11:
            print("\nYou are very close !\n")
        elif 10 < distance < 21:
            print("\nYou are close !\n")
        elif 20 < distance < 36:
            print("\nNot too far !\n")
        elif 35 < distance < 56:
            print("\nYou are far away !\n")
        elif 55 < distance < 76:
            print("\nYou are very far away !\n")
        else:
            print("\nNowhere near it !\n")        

def level_01():
    
    while True:
        
        try:
            
            ans01 = int(input("What's the number: "))
            
            difference01 = abs(secret_number - ans01)

            if 1 <= ans01 <= 10:
                
                if ans01 == secret_number:
                    print("\nCorrect !")
                    print("\nYou won the game !\n")
                    return
             
                else:
                    compare(difference01, chosen_level)
                    print("Try again.\n")    
            
            else:
                print("Please enter a number fom 1 to 10 !! ")
        
        except ValueError:
            print("Please enter a 'number' fom 1 to 10 !! ")

def level_02(): 
    
    for n in range(levels[chosen_level]['tries']):    
        
        remaining = levels[chosen_level]['tries'] - n - 1
        
        while True:
        
            try:

                ans02 = int(input("What's the number:  "))

                difference02 = abs(secret_number - ans02)
                
                if 1 <= ans02 <= levels[chosen_level]['max']:    
                    
                    if ans02 == secret_number:
                        print("\nCorrect !")
                        print("\nYou won the game !\n")
                        return
                    
                    elif remaining > 0:
                        compare(difference02, chosen_level)
                        print("Try again.\n")
                        print(f"Attempts remaining: {remaining} !")    

                    break    
                
                else:
                    print(f"Please enter a number fom 1 to {levels[chosen_level]['max']} !! ")        
            
            except ValueError:
                print(f"Please enter a 'number' fom 1 to {levels[chosen_level]['max']} !! ")  
    print("\nYou lose !\n")
    print(f"The secret number was {secret_number} !!\n")      

def restart():

    while True:

        menu = input("To play again press 'A' or to exit press 'B':  ").strip().upper()

        match menu:

            case "A":
                return True
            case "B":
                print()
                exit()
            case _:
                print("\nPlease choose from 'A' or 'B' !!\n") 

print("\nHi there, this is a simple number guessing game.")

rules()

while True:

    chosen_level = level()   

    chosen_level = re_level(chosen_level)

    secret_number = random.randint(1,levels[chosen_level]['max']) 

    print("\nGAME START\n")

    if chosen_level == 1: 
        level_01()
        if restart():
            continue

    else:
        level_02()
        if restart():
            continue