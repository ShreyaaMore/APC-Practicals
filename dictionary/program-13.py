# 13.	Create a dictionary containing student names and marks. Calculate the average marks of all students.

student_marks = {
    "Mikhil": 91,
    "Ravi": 60,
    "Shreya": 95,
    "Jignesh": 80,
    "Kirito": 96
}

avg = sum(marks for student, marks in student_marks.items()) / len(student_marks)

print("Student Marks:", student_marks)
print("Students Average Marks:", avg)
