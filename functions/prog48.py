employees = [
    {"name": "Alice", "salary": 65000},
    {"name": "Bob", "salary": 45000},
    {"name": "Charlie", "salary": 80000},
    {"name": "Diana", "salary": 55000}
]
sorted_employees = sorted(employees, key=lambda e: e["salary"])
print(sorted_employees)
