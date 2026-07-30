# Write a program to input a string and display its length without using the len() function. 

s = input("Enter a string: ")
count = 0

for i in s:
    count += 1

print(f"The length of the given string is {count}.")