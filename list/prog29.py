# Store temperature of 30 days and determine:
# 1. Hottest day
# 2. Coldest day
# 3. Average temperature
# 4. Days above average temperature
# 5. Days below average temperature

temperature = [30, 32, 29, 35, 34, 31, 33, 36, 28, 30,
               31, 34, 35, 37, 29, 30, 32, 33, 34, 35,
               31, 30, 29, 28, 36, 37, 33, 32, 31, 30]

while True:

    print("\n1. Hottest day\n2. Coldest day\n3. Average temperature\n4. Days above average temperature\n5. Days below average temperature\n6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        hottest = max(temperature)
        print("Hottest temperature:", hottest, "°C")

    elif choice == 2:
        coldest = min(temperature)
        print("Coldest temperature:", coldest, "°C")

    elif choice == 3:
        average = sum(temperature) / len(temperature)
        print("Average temperature:", average, "°C")

    elif choice == 4:
        average = sum(temperature) / len(temperature)
        count = 0

        for i in temperature:
            if i > average:
                count += 1

        print("Days above average temperature:", count)

    elif choice == 5:
        average = sum(temperature) / len(temperature)
        count = 0

        for i in temperature:
            if i < average:
                count += 1

        print("Days below average temperature:", count)

    elif choice == 6:
        print("Program Ended")
        break

    else:
        print("Invalid input")