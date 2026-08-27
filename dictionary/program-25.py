# 25. Create a dictionary containing student names and marks. Develop a program to:
# • Add a student • Update marks • Delete a student • Search for a student
# • Display all students • Find the highest marks • Calculate the average

students = {
    "Alice": 85,
    "Bob": 92, 
    "Charlie": 78
}

def add_student(name, marks):
    students[name] = marks
    print(f"Added student {name}.")

def update_marks(name, marks):
    if name in students:
        students[name] = marks
        print(f"Updated marks for {name}.")
    else:
        print(f"Student {name} not found.")

def delete_student(name):
    if name in students:
        del students[name]
        print(f"Deleted student {name}.")
    else:
        print(f"Student {name} not found.")

def search_student(name):
    if name in students:
        print(f"Student: {name}, Marks: {students[name]}")
    else:
        print(f"Student {name} not found.")

def display_students():
    print("All students:")
    for name, marks in students.items():
        print(f"{name}: {marks}")

def highest_marks():
    if not students:
        return None
    highest = max(students.values())
    top_students = [name for name, marks in students.items() if marks == highest]
    print(f"Highest marks: {highest} by {', '.join(top_students)}")

def calculate_average():
    if not students:
        return 0
    avg = sum(students.values()) / len(students)
    print(f"Average marks: {avg:.2f}")


display_students()
add_student("David", 95)
update_marks("Alice", 88)
delete_student("Charlie")
search_student("Bob")
display_students()
highest_marks()
calculate_average()
