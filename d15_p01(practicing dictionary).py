data = {
    1: {"Name": "Rahul", "Age": 18, "Marks": 98},
    2: {"Name": "Rohit", "Age": 20, "Marks": 97},
    3: {"Name": "Ramesh", "Age": 18, "Marks": 90},
    4: {"Name": "Rakesh", "Age": 19, "Marks": 79}
}


print("\nThe names of the students are:")
for student in data.values():
    print(student["Name"])

print("\nThe names of the students again are:")
for student in data:
    print(data[student]["Name"])


print("The marks of the students are:")
for mark in data.values():
    print(mark["Marks"])

print("The marks of the students again are:")
for mark in data:
    print(data[mark]["Marks"])

edit = input("Enter the name of the student, whose marks you want to change: ").strip().capitalize()
for student in data.values():
    if student["Name"] == edit:
        print(f"Current marks: {student['Marks']}")
        new = int(input("Enter new marks: "))
        student["Marks"] = new

print("Updated student marks are: ")
for n, student in enumerate(data.values(), start= 1):
    print(f"{n}) {student['Name']} : {student['Marks']}")

print("enter the city of students")
data[1]['City'] = input("Rahul: ").strip().capitalize()
data[2]['City'] = input("Rohit: ").strip().capitalize()
data[3]['City'] = input("Ramesh: ").strip().capitalize()
data[4]['City'] = input("Rakesh: ").strip().capitalize()

print("ages are removed")
for student in data.values():
    student.pop('Age')

print("The final data is:")

for n, student in enumerate(data.values(), start = 1):
    print(f"{n}) {student['Name']}\nMarks: {student['Marks']}\nCity: {student['City']}\n ")