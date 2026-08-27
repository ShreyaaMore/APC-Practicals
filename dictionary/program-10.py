# 10.	Accept five student names and their marks from the user and store them in a dictionary.

students_marks = {}

print("Enter details for 5 students:")
for i in range(5):
    print(f"Enter student {i+1} Details:")
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))
    students_marks[name] = marks

print(f"Students Marks details: {students_marks}")