employees = [
    {"name": "John", "dept": "IT", "salary": 60000},
    {"name": "Jane", "dept": "HR", "salary": 45000},
    {"name": "Mark", "dept": "Finance", "salary": 75000},
    {"name": "Lucy", "dept": "Marketing", "salary": 48000}
]

high_earners = list(filter(lambda e: e["salary"] > 50000, employees))
print("Employees earning > 50000:", high_earners)

updated_salaries = list(map(lambda e: {**e, "salary": e["salary"] * 1.10}, employees))
print("Salaries increased by 10%:", updated_salaries)

sorted_by_salary = sorted(employees, key=lambda e: e["salary"])
print("Employees sorted by salary:", sorted_by_salary)
