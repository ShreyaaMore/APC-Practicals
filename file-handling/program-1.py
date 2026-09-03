# 1.	Write a Python program to create a file named student.txt and write the student's name, roll number, branch, and semester into the file.

name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")
branch = input("Enter Branch: ")
semester = input("Enter Semester: ")

with open("student.txt", "w") as f:
    f.write(f"Name: {name}\n")
    f.write(f"Roll No: {roll_no}\n")
    f.write(f"Branch: {branch}\n")
    f.write(f"Semester: {semester}\n")

print("Student details written to student.txt successfully.")

