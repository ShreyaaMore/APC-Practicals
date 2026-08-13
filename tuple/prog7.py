# 	Create a tuple of employee IDs and find the index of a given ID.

employee_ids = (101,102,103,104,105,106)

id = int(input("Enter Employee ID to find: "))

if id in employee_ids:
    print(f"Employee found at index {employee_ids.index(id)}")
else:
    print("Employee ID not found.")