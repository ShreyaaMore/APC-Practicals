# 12.	Create a dictionary containing student names and marks. Find the student with the lowest marks.

student_marks = {
    "Mikhil": 91,
    "Ravi": 60,
    "Shreya": 95,
    "Jignesh": 80,
    "Kirito": 96
}

print("Student Marks:", student_marks)

min_marks = 100
min_marks_std = ""

for student, marks in student_marks.items():
    if marks < min_marks:
        min_marks = marks
        min_marks_std = student


print(f"Student with Lowest marks {min_marks} is {min_marks_std}")