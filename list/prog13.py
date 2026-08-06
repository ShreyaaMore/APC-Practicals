# 13.	Accept 10 numbers and sort them in:
# •	Ascending order 
# •	Descending order

lst = []

print("Enter 10 numbers.")
for i in range(10):
    n = int(input(f"Enter number {i+1}: "))
    lst.append(n)


print(f"Entered Numbers: {lst}")
lst.sort()
print(f"Ascending Order: {lst}")
lst.sort(reverse=True)
print(f"Descending Order: {lst}")
