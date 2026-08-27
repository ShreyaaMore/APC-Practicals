students = {"Alice", "Bob", "Charlie", "David", "Eve"}
name = input("Enter student name to search: ")
if name in students:
    print(f"{name} is present in the set.")
else:
    print(f"{name} is not present in the set.")
