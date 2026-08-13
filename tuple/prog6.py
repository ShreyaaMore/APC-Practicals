# Create a tuple with repeated numbers and count how many times a particular number appears.

num = (1,5,3,4,1,2,6,5,8,3,7,9,1,6,3,2,4)

target = int(input("Enter a number to count: "))

count = num.count(target)

print(f"{target} occurs {count} times in the tuple.")