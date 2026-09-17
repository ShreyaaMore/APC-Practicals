# 11.	Create a base class Student with attributes roll_no, name, and course. Derive a class Result that stores marks in three subjects and calculates total marks, percentage, and grade.

class Student:
    def __init__(self, roll_no, name, course):
        self.roll_no = roll_no
        self.name = name
        self.course = course

    def display_student(self):
        print(f"Roll Number : {self.roll_no}")
        print(f"Name        : {self.name}")
        print(f"Course      : {self.course}")


class Result(Student):
    def __init__(self, roll_no, name, course, sub1, sub2, sub3):
        super().__init__(roll_no, name, course)
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3

    def calculate_total(self):
        return self.sub1 + self.sub2 + self.sub3

    def calculate_percentage(self):
        return (self.calculate_total() / 300) * 100

    def calculate_grade(self):
        pct = self.calculate_percentage()
        if pct >= 90:
            return "A+"
        elif pct >= 80:
            return "A"
        elif pct >= 70:
            return "B"
        elif pct >= 60:
            return "C"
        elif pct >= 50:
            return "D"
        else:
            return "F (Fail)"

    def display_result(self):
        print("Student Result")
        self.display_student()
        print(f"Marks       : Subject 1 = {self.sub1}, Subject 2 = {self.sub2}, Subject 3 = {self.sub3}")
        print(f"Total Marks : {self.calculate_total()} / 300")
        print(f"Percentage  : {self.calculate_percentage():.2f}%")
        print(f"Grade       : {self.calculate_grade()}\n")


res = Result(106, "Shreya More", "Computer Science", 92, 88, 95)
res.display_result()
