# Print the first and last character of a string.

s = input("Enter a string: ")

if len(s) > 0:
    
    first = s[0]
    last = s[-1]

    print(f"The First character of the given string is: {first}")
    print(f"Last character: {last}")
else:
    print("String is empty.")