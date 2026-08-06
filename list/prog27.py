# Store salaries of employees and determine:
# 1. Highest salary
# 2. Lowest salary
# 3. Average salary
# 4. Employees earning above ₹50,000
# 5. Employees earning below ₹30,000

salaries = [25000, 32000, 45000, 55000, 60000,
            28000, 75000, 48000, 51000, 29000]

while True:

    print("\n1. Highest salary\n2. Lowest salary\n3. Average salary\n4. Employees earning above ₹50,000\n5. Employees earning below ₹30,000\n6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        highest = max(salaries)
        print("Highest salary: ₹", highest)

    elif choice == 2:
        lowest = min(salaries)
        print("Lowest salary: ₹", lowest)

    elif choice == 3:
        average = sum(salaries) / len(salaries)
        print("Average salary: ₹", average)

    elif choice == 4:
        count = 0
        for i in salaries:
            if i > 50000:
                count += 1
        print("Employees earning above ₹50,000:", count)

    elif choice == 5:
        count = 0
        for i in salaries:
            if i < 30000:
                count += 1
        print("Employees earning below ₹30,000:", count)

    elif choice == 6:
        print("Program Ended")
        break

    else:
        print("Invalid input")