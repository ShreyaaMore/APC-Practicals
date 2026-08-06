# Write a program to find the largest and smallest number in a list without using max() or min().

l = [15, 25, 10, 5, 45, 30]

max = l[0]
min = l[0]

for i in l:
    if i>max:
        max = i
    if i<min:
        min = i

print(f"The largest number is {max} and the smallest number is {min}.")