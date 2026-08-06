# 	Create a list of numbers. Add:
# •	One element at the end 
# •	One element at the beginning 
# •	One element at a specified position 
# Display the updated list.

nums = [20, 30, 40, 50, 60, 70]

print("Original list: ", nums)

nums.append(80)
nums.insert(0,10)
nums.insert(4,100)

print("Updated list: ", nums)