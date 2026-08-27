# 4.	Create a dictionary containing student marks. Update the marks of a specified student.

student_marks = {
    "Mikhil": 91,
    "Ravi": 60,
    "Shreya": 95,
    "Jignesh": 80
}

print("Students Marks:", student_marks)

std_update = input("Enter student name to update the marks: ")

if std_update in student_marks:
    student_marks[std_update] = int(input("Enter marks: "))
    print("\nStudent Marks:", student_marks)
else:
    print("No such student.")