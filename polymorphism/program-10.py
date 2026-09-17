# 10.	Create a class Student containing the student's name and total marks. Overload the > and < operators to compare the marks of two students.

class Student:
    def __init__(self, name, total_marks):
        self.name = name
        self.total_marks = total_marks

    def __gt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.total_marks > other.total_marks

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.total_marks < other.total_marks

    def __str__(self):
        return f"{self.name} ({self.total_marks} marks)"


s1 = Student("Amit", 465)
s2 = Student("Priya", 488)

print("Operator Overloading: Student Comparisons (< and >)")
print(f"Student 1: {s1}")
print(f"Student 2: {s2}\n")

if s1 > s2:
    print(f"{s1.name} scored more marks than {s2.name}.")
elif s1 < s2:
    print(f"{s2.name} scored more marks than {s1.name}.")
else:
    print("Both students scored equal marks.")
