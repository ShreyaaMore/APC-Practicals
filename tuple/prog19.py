# Store 15 integers in a tuple and count:
# •	Even numbers 
# •	Odd numbers

numbers = (12,53,24,69,75,21,40,75,81,35,60,75,41,88,57)

odd = 0
even = 0

for i in numbers:
    if i%2==0:
        even+=1
    else:
        odd+=1

print(f"Number of even numbers = {even}\nNumber of odd numbers = {odd}")