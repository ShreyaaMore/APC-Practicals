# Count the frequency of each element in a tuple.

numbers = (10, 20, 10, 30, 20, 10, 40, 30)

for item in set(numbers):
    print(item, ":", numbers.count(item))