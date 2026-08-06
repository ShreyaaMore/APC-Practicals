# Count the frequency of each element in a list.

list1 = [10, 20, 10, 30, 20, 10, 40]

checked = []

for i in list1:
    if i not in checked:
        count = 0
        for j in list1:
            if i == j:
                count += 1
        print(i, "occurs", count, "times")
        checked.append(i)