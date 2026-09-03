# 3.	Write a program to append additional student information to an existing file without deleting its previous contents.

name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")
branch = input("Enter Branch: ")
semester = input("Enter Semester: ")

with open("student.txt", "a") as f:
    f.write(f"\nName: {name}\n")
    f.write(f"Roll No: {roll_no}\n")
    f.write(f"Branch: {branch}\n")
    f.write(f"Semester: {semester}\n")

print("Additional student details appended to student.txt successfully.")

