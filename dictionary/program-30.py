# 30. Take a dictionary containing student names and their departments; create a new dictionary that groups students according to their department.

students = {
    "Alice": "Computer Science",
    "Bob": "Mathematics",
    "Charlie": "Computer Science",
    "David": "Physics",
    "Eve": "Mathematics"
}

department_groups = {}
for name, dept in students.items():
    if dept not in department_groups:
        department_groups[dept] = []
    department_groups[dept].append(name)

print("Original students dictionary:")
print(students)
print("\nGrouped by department:")
print(department_groups)
