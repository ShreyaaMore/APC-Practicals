students = [
    {"name": "Alice", "marks": 85},
    {"name": "Bob", "marks": 70},
    {"name": "Charlie", "marks": 92},
    {"name": "David", "marks": 60},
    {"name": "Eve", "marks": 78}
]

def calculate_average(records):
    return sum(map(lambda s: s["marks"], records)) / len(records)

avg = calculate_average(students)
print("Average Marks:", avg)

above_75 = list(filter(lambda s: s["marks"] > 75, students))
print("Students scoring above 75:", above_75)

sorted_students = sorted(students, key=lambda s: s["marks"])
print("Students sorted by marks:", sorted_students)
