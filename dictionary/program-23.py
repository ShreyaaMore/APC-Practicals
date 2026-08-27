# 23. Given a list of numbers, create a dictionary containing each unique number and its frequency.

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5]

frequency = {}
for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print("List of numbers:", numbers)
print("Frequency dictionary:")
print(frequency)
