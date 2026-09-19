print()
print("THIS DEVICE IS A VERY SIMPLE ODD AND EVEN CHECKER:")
print()

while True:
 
 a=(input("Please give an integer to check for: "))
 print()

 if a.isdigit():
      
       a = int(a)
       if a % 2 == 0:
           print("The given integer is even.")
       else: 
           print("The given integer is odd")
       print()
       print("Thank you for using our device.")
       print()
       break
 
 else:
       print("Please enter a valid integer value")
       print()
