# 26. Create a dictionary containing employee names and salaries. Find:
# • Highest salary 
# • Lowest salary 
# • Average salary 
# • Employees earning more than ₹50,000

employees = {
    "John": 45000,
    "Emma": 62000,
    "Michael": 55000,
    "Sophia": 48000,
    "William": 70000
}

highest = max(employees.values())
lowest = min(employees.values())
average = sum(employees.values()) / len(employees)
high_earners = [name for name, salary in employees.items() if salary > 50000]

print("Employees:", employees)
print("Highest salary:", highest)
print("Lowest salary:", lowest)
print(f"Average salary: {average:.2f}")
print("Employees earning more than ₹50,000:", ", ".join(high_earners))
