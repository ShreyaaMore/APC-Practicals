# Find the second most frequently occurring character.

s = input("Enter a string: ")

freq = {}
for char in s:
    freq[char] = freq.get(char, 0) + 1

counts = sorted(set(freq.values()), reverse=True)

if len(counts) >= 2:
    second_highest = counts[1]  # [0] is the highest, [1] is the second highest
    
    for char, count in freq.items():
        if count == second_highest:
            print(f"Second most frequent: '{char}' (Appears {count} times)")
else:
    print("There is no second most frequent character.")