# 8.	Store 15 integers in a list. Count how many numbers are:
# •	Even 
# •	Odd

num = [24, 53, 86, 20, 47, 68 ,75, 14, 22, 55, 74, 37, 11, 59, 82]

print(f"Numbers: {num}")

odd = 0
even = 0
for i in num:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print(f"Count of odd Numbers: {odd}\nCount of even Numbers: {even}")