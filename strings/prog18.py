# Remove duplicate characters while maintaining the original order.

s = input("Enter a string: ")
result_list = []
seen = set()

for char in s:
    if char not in seen:
        seen.add(char)
        result_list.append(char)

result = "".join(result_list)

print(f"String after removing duplicates: {result}")