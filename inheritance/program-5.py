# 5.	Create a class Person containing name and age. Derive a class Student from Person with roll number and course. Further derive a class ResearchStudent from Student with research topic and guide name. Display all details.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print(f"Name           : {self.name}")
        print(f"Age            : {self.age}")


class Student(Person):
    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course

    def display_student(self):
        self.display_person()
        print(f"Roll Number    : {self.roll_no}")
        print(f"Course         : {self.course}")


class ResearchStudent(Student):
    def __init__(self, name, age, roll_no, course, research_topic, guide_name):
        super().__init__(name, age, roll_no, course)
        self.research_topic = research_topic
        self.guide_name = guide_name

    def display_research_student(self):
        print("Research Student Details")
        self.display_student()
        print(f"Research Topic : {self.research_topic}")
        print(f"Guide Name     : {self.guide_name}\n")


rs = ResearchStudent("Aditi Kulkarni", 25, "PHD-102", "Computer Engineering", "Neural Architecture Search", "Dr. S. K. Nair")
rs.display_research_student()
