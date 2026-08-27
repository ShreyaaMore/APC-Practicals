# 32. Take a list of integers and a target value, find two numbers whose sum is equal to the target using a dictionary.

numbers = [2, 7, 11, 15]
print("Numbers:", numbers)
taget = int(input("Enter a target number: "))


def find_two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return complement, num
        seen[num] = i
    return None

result = find_two_sum(numbers, target)
print(f"Numbers: {numbers}")
print(f"Target sum: {target}")
if result:
    print(f"Two numbers that add up to target: {result[0]} and {result[1]}")
else:
    print("No such pair found.")
