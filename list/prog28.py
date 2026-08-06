# Store scores of a batsman in 10 matches and calculate:
# 1. Highest score
# 2. Lowest score
# 3. Total runs
# 4. Average runs
# 5. Number of centuries (>=100)
# 6. Number of half-centuries (50-99)

scores = [45, 102, 67, 89, 120, 34, 56, 100, 78, 15]

while True:

    print("\n1. Highest score")
    print("2. Lowest score")
    print("3. Total runs")
    print("4. Average runs")
    print("5. Number of centuries")
    print("6. Number of half-centuries")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        highest = max(scores)
        print("Highest score:", highest)

    elif choice == 2:
        lowest = min(scores)
        print("Lowest score:", lowest)

    elif choice == 3:
        total = sum(scores)
        print("Total runs:", total)

    elif choice == 4:
        average = sum(scores) / len(scores)
        print("Average runs:", average)

    elif choice == 5:
        count = 0
        for i in scores:
            if i >= 100:
                count += 1
        print("Number of centuries:", count)

    elif choice == 6:
        count = 0
        for i in scores:
            if i >= 50 and i <= 99:
                count += 1
        print("Number of half-centuries:", count)

    elif choice == 7:
        print("Program Ended")
        break

    else:
        print("Invalid input")