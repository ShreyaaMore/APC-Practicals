# 9.	Create a class Person. Derive Student and Faculty from Person. Create another class TeachingAssistant that inherits from both Student and Faculty. Display the details and demonstrate the use of multiple and hierarchical inheritance together.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print(f"Name : {self.name}")
        print(f"Age  : {self.age}")


class Student(Person):
    def __init__(self, name, age, student_id, program):
        Person.__init__(self, name, age)
        self.student_id = student_id
        self.program = program

    def display_student(self):
        print(f"Student ID : {self.student_id}")
        print(f"Program    : {self.program}")


class Faculty(Person):
    def __init__(self, name, age, faculty_id, department):
        Person.__init__(self, name, age)
        self.faculty_id = faculty_id
        self.department = department

    def display_faculty(self):
        print(f"Faculty ID : {self.faculty_id}")
        print(f"Department : {self.department}")


class TeachingAssistant(Student, Faculty):
    def __init__(self, name, age, student_id, program, faculty_id, department, stipend):
        Student.__init__(self, name, age, student_id, program)
        Faculty.__init__(self, name, age, faculty_id, department)
        self.stipend = stipend

    def display_ta_details(self):
        print("Teaching Assistant Details (Hybrid Inheritance)")
        self.display_person()
        self.display_student()
        self.display_faculty()
        print(f"Stipend    : Rs. {self.stipend:.2f}\n")


ta = TeachingAssistant("Arjun Dixit", 24, "STU-882", "M.Tech CSE", "FAC-TA-12", "Computer Science", 25000.0)
ta.display_ta_details()
