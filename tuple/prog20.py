# Accept a number from the user and determine whether it exists in the tuple.

numbers = (45,36,71,24,85,96,10,24,56,85,77,42,58,39)

n = int(input("Enter a number: "))

if n in numbers:
    print(f"{n} exists in the tuple")
else:
    print(f"{n} does not exist in the tuple")