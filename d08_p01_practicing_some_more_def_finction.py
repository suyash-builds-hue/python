def fibonacci(n):
        """Print a Fibonacci series less than n."""
        print()
        a, b = 0, 1
        while a < n :
            
            print(a, end=" ")
            a, b = b, a+b
        print()    


def arit_progreson(p):
        """Printing an AP of p terms"""
        
        while True:
            try:
                print()
                a = float(input("What's the first term of the AP: "))
                d = float(input("What's the common difference: "))
                print()
                if p > 0:
                    q = a
                    terms = []
                    for i in range(p):
                        q = q + d
                        terms.append(str(q))
                    print()
                    print(", ".join(terms))
                    print()
                    break
                else:
                    print()                  
                    print("The value of p can't be negative !!")
                    print()
            except ValueError:
                print()
                print("Please enter valid values !!")
                print()
        
print()
print("What do you want a fibonacci till 1000, \nor an arithmetic progression of 10 terms?")
print()

while True:    
    choice = input("Press 'F' for fibonacci or press 'A' for arithmetic progression.  ").upper().strip()
    match choice:
        case "F":
            print()
            fibonacci(1000)
            print()
            break
        case "A":
            print()
            arit_progreson(10)
            print()
            break
        case _:
            print()
            print("Please choose from 'F' and 'A' !!")
            print()