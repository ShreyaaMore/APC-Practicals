def unique_elements(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

l = [10, 20, 10, 30, 40, 20, 50, 30]
print("Unique elements:", unique_elements(l))