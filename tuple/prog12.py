# Accept five numbers from the user, store them in a list, and convert the list into a tuple.

num = []
for i in range(5):
    n = int(input(f"Enter number {i+1}: "))
    num.append(n)

print(tuple(num))