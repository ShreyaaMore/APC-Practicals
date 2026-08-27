# 8.	Create a dictionary and display:
# •	All keys 
# •	All values 
# •	All key-value pairs


students = {
    101: "Mikhil",
    102: "Shreya",
    103: "Ravi",
    104: "Jignesh",
    105: "Tom"
}

print("Student details:")

for student in students:
    print(f"Roll No. (key): {student}")
    print(f"Name(value): {students[student]}")
    print(f"(key-value): {student} - {students[student]}")
    print()