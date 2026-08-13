# Find the largest and smallest number in a tuple without using max() and min().

numbers = (21,53,42,62,82,15,64,72,10,65,95)
min = numbers[0]
max = numbers[0]

for i in numbers:
    if i > max:
        max = i
    if i < min:
        min = i

print("The largest number is",max)
print("The smallest number is", min)