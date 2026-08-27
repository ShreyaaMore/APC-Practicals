def count_occurrences(lst, element):
    count = 0
    for item in lst:
        if item == element:
            count += 1
    return count

l = [10, 20, 30, 20, 40, 20, 50]
element = 20
print("Occurrences:", count_occurrences(l, element))
