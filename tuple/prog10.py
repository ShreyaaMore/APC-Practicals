# Create a tuple of 10 numbers and display:
# •	First five elements 
# •	Last five elements 
# •	Middle four elements 
# •	Alternate elements 
# •	Reverse tuple

numbers = (10,20,30,40,50,60,70,80,90,100)

print(f"First five elements: {numbers[0:5]}")
print(f"Last five elements: {numbers[5:]}")
print(f"Middle four elements: {numbers[3:7]}")
print(f"Alternate elements: {numbers[0::2]}")
print(f"Reversed tiple: {numbers[::-1]}")
