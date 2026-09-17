# 16.	Create a class Person with name and age. Derive Student with roll number and course. Further derive ResearchStudent with research topic and guide name.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"I am {self.name}, {self.age} years old.")


class Student(Person):
    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course

    def study(self):
        print(f"Enrolled in {self.course} with Roll Number: {self.roll_no}.")


class ResearchStudent(Student):
    def __init__(self, name, age, roll_no, course, research_topic, guide_name, publications_count=0):
        super().__init__(name, age, roll_no, course)
        self.research_topic = research_topic
        self.guide_name = guide_name
        self.publications_count = publications_count

    def conduct_research(self):
        self.introduce()
        self.study()
        print(f"Conducting research on '{self.research_topic}' under the guidance of {self.guide_name}.")
        print(f"Total Publications: {self.publications_count}\n")


researcher = ResearchStudent("Meera Joshi", 26, "PHD-509", "Data Science", "Explainable AI in Healthcare", "Dr. Rajesh Iyer", 4)
print("Research Student Overview")
researcher.conduct_research()
