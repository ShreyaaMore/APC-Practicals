# 19.	Store student attendance records in a file. Calculate the attendance percentage and display students having attendance below 75%.

import os

filename = "attendance.txt"

if not os.path.exists(filename):
    with open(filename, "w") as f:
        f.write("RollNo,Name,TotalClasses,AttendedClasses\n")
        f.write("101,Aman,50,45\n")
        f.write("102,Bhavna,50,32\n")
        f.write("103,Chetan,50,42\n")
        f.write("104,Divya,50,30\n")
        f.write("105,Esha,50,48\n")
    print(f"Sample attendance records created in '{filename}'.")

print("\nStudent Attendance Report:")
print(f"{'Roll No':<10} {'Name':<15} {'Attended/Total':<18} {'Percentage':<12}")
print()

below_75 = []

with open(filename, "r") as f:
    f.readline()
    for line in f:
        line = line.strip()
        if line:
            roll_no, name, total, attended = line.split(",")
            total_classes = int(total)
            attended_classes = int(attended)
            percentage = (attended_classes / total_classes) * 100

            print(f"{roll_no:<10} {name:<15} {f'{attended_classes}/{total_classes}':<18} {percentage:.2f}%")

            if percentage < 75.0:
                below_75.append((roll_no, name, percentage))

print("\nStudents with Attendance Below 75%:")
if below_75:
    for roll_no, name, percentage in below_75:
        print(f"Roll No: {roll_no}, Name: {name}, Attendance: {percentage:.2f}%")
else:
    print("No students have attendance below 75%.")

