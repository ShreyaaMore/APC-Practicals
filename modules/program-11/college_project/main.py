# 11.	Create the following directory structure: 
# a)	college_project/
# b)	main.py
# c)	student/
# d)	__init__.py
# e)	details.py
# f)	marks.py
# g)	faculty/
# h)	__init__.py
# i)	details.py
# Write a program that imports functions from both packages and displays student and faculty information.

from student.details import get_student_details, display_student_info
from student.marks import get_student_marks, display_student_marks
from faculty.details import get_faculty_details, display_faculty_info

print("College Project Management System:\n")

student = get_student_details(105, "Shreya More", "Computer Science", 5)
display_student_info(student)

marks_data = {
    "Advanced Programming": 95,
    "Operating Systems": 88,
    "Database Management": 92,
    "Computer Networks": 89
}
student_marks = get_student_marks(marks_data)
display_student_marks(student_marks)

print("\n" + "=" * 40 + "\n")

faculty = get_faculty_details("FAC201", "Dr. A. Sharma", "Computer Science", "Professor")
display_faculty_info(faculty)

