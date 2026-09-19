# Practicing numeric or number/digit related functions :--
a=(input("give in some positive integer"))
if a.isdigit():
    print("you have given a positive integer")
    a=int(a)

b=float(input("give in a decimal number"))
print("on rounding to nearest 4 digits we get", round(b, 4))

print(" product of the 2 numbers give", a*b)
print("addition of the 2 numbers give", a+b)
print("on subtracting second from first number we get", a-b)
if b==0:
    print("division by 0 is not possible")
else:
    print("dividing second from first we get", a/b)
