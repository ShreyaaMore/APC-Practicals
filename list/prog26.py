# Store marks of 20 students in a list and determine:
# 1. Highest marks
# 2. Lowest marks
# 3. Average marks
# 4. Number of students scoring above average
# 5. Number of students scoring below average

marks = [98, 75, 68, 84, 88, 91, 74, 70, 85, 65,
         73, 99, 65, 71, 85, 66, 44, 79, 91, 82]

while True:

    print("\n1. Highest marks")
    print("2. Lowest marks")
    print("3. Average marks")
    print("4. Number of students scoring above average")
    print("5. Number of students scoring below average")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        highest = max(marks)
        print("Highest marks:", highest)

    elif choice == 2:
        lowest = min(marks)
        print("Lowest marks:", lowest)

    elif choice == 3:
        average = sum(marks) / len(marks)
        print("Average marks:", average)

    elif choice == 4:
        average = sum(marks) / len(marks)
        count = 0

        for i in marks:
            if i > average:
                count += 1

        print("Students scoring above average:", count)

    elif choice == 5:
        average = sum(marks) / len(marks)
        count = 0

        for i in marks:
            if i < average:
                count += 1

        print("Students scoring below average:", count)

    elif choice == 6:
        print("Program Ended")
        break

    else:
        print("Invalid input")