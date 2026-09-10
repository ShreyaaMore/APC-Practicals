# 1.	Create a class Student with attributes such as roll_no, name, and marks. Create objects for multiple students and display their details and percentage.

class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def calculate_percentage(self):
        if not self.marks:
            return 0.0
        return (sum(self.marks) / (len(self.marks) * 100)) * 100

    def display_details(self):
        print(f"Roll No    : {self.roll_no}")
        print(f"Name       : {self.name}")
        print(f"Marks      : {self.marks}")
        print(f"Percentage : {self.calculate_percentage():.2f}%\n")


s1 = Student(101, "Amit Sharma", [85, 90, 78, 88, 92])
s2 = Student(102, "Priya Patil", [92, 95, 89, 94, 91])
s3 = Student(103, "Rahul Verma", [72, 68, 75, 80, 70])

print("Student Details")
s1.display_details()
s2.display_details()
s3.display_details()
