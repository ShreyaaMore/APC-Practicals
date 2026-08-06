# 11.	Create a list of 10 numbers and display:
# •	First 5 elements 
# •	Last 5 elements 
# •	Middle 4 elements 
# •	Alternate elements 

numbers = [74,58,63,95,21,74,10,81,72,43]

print(f"First 5 Elements: {numbers[:5]}")
print(f"Last 5 Elements: {numbers[-5:]}")
print(f"Mid 4 Elements: {numbers[3:-3]}")
print(f"Alternate Elements: {numbers[::2]}")
print(f"Reversed List: {numbers[::-1]}")