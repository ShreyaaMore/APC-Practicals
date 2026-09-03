# 17.	Create a file containing student records in the format:
# RollNo,Name,Marks
# 101,Amit,85
# 102,Priya,92
# 103,Rahul,78
# Write a program to:
# •	Display all records. 
# •	Find the student with the highest marks. 
# •	Calculate average marks. 
# •	Display students who scored more than 80.

import os

filename = "student_records.txt"

if not os.path.exists(filename):
    with open(filename, "w") as f:
        f.write("RollNo,Name,Marks\n")
        f.write("101,Amit,85\n")
        f.write("102,Priya,92\n")
        f.write("103,Rahul,78\n")
    print(f"Sample file '{filename}' created.")

records = []
with open(filename, "r") as f:
    header = f.readline().strip().split(",")
    for line in f:
        line = line.strip()
        if line:
            parts = line.split(",")
            records.append({
                "RollNo": parts[0],
                "Name": parts[1],
                "Marks": float(parts[2])
            })

print("\nAll Student Records:")
print(f"{'Roll No':<10} {'Name':<15} {'Marks':<10}")
print()
for r in records:
    print(f"{r['RollNo']:<10} {r['Name']:<15} {r['Marks']:<10}")

highest_student = max(records, key=lambda x: x["Marks"])
print(f"\nStudent with the highest marks: {highest_student['Name']} (Marks: {highest_student['Marks']})")

avg_marks = sum(r["Marks"] for r in records) / len(records)
print(f"\nAverage marks of the class: {avg_marks:.2f}")

print("\nStudents who scored more than 80:")
for r in records:
    if r["Marks"] > 80:
        print(f"- {r['Name']} (Roll No: {r['RollNo']}, Marks: {r['Marks']})")

