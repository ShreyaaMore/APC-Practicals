python_students = {"Alice", "Bob", "Charlie", "David"}
java_students = {"Charlie", "David", "Eve", "Frank"}
both_courses = python_students.intersection(java_students)
only_one_course = python_students.symmetric_difference(java_students)
print("Python Students:", python_students)
print("Java Students:", java_students)
print("Enrolled in both courses:", both_courses)
print("Enrolled in only one course:", only_one_course)
