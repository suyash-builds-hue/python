students = ["Rahul", "Rohit", "Ramesh", "Rakesh"]



print("\nThe students are:")
print(students[0])
print(students[1])
print(students[2])  
print(students[3])

print("\nFirst student is:", students[0])
print("\nLast student is:", students[3])


add = input("\nEnter the name of the student to add: ").strip().capitalize()
students.append(add)

print("\nUpdated list of students:")
print(students[0])
print(students[1])
print(students[2])
print(students[3])
print(students[4])

remove = input("\nEnter the name of the student to remove: ").strip().capitalize()
students.remove(remove)

print("\nUpdated list of students after removal:")
print(students[0])
print(students[1])
print(students[2])
print(students[3])

length = len(students)
print("\nTotal number of students:", length)

students.sort()

print("\nAlphabetically sorted list of students:")
for student in students:
    print(student)

print("\nFirst 3 students in the sorted list:")
print(students[0:3])

print("\nLast 2 students in the sorted list:")
print(students[-2:])

print("\nThe reversed list of students is:")
for student in reversed(students):
    print(student)

print("\nThe reversed list of students again is:")
for student in range(len(students)-1,-1,-1):
    print(student)

print("\nThe reversed list of students again is:")
print(students[::-1])

