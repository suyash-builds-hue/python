# Practicing different str functions :--

print()
a=input("Enter your name can be of only 2 parts ").strip().title()
first, last=a.split(" ")
b=input("Enter school name  ").capitalize().strip()
print()
print("First name: ", first)
print()
print("Last name : ", last)
print()
print("The name of the school is: ", b)
print()
c=input("random alphabets; true if all are alphabets ")
print()
if c.isalpha():
    print(True)
else:
    print(False)
d=input("random alphabets; true if all are in lowercase  ")
if d.islower():
    print(True)
else:
    print(False)
