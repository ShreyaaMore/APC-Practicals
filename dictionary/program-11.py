# 11.	Create a dictionary containing student names and marks. Find the student who has scored the highest marks.


student_marks = {
    "Mikhil": 91,
    "Ravi": 60,
    "Shreya": 95,
    "Jignesh": 80,
    "Kirito": 96
}

print("Student Marks:", student_marks)

max_marks = 0
max_marks_std = ""

for student, marks in student_marks.items():
    if marks > max_marks:
        max_marks = marks
        max_marks_std = student


print(f"Student with highest marks {max_marks} is {max_marks_std}")