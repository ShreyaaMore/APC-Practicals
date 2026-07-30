# Compress a string by counting consecutive repeated characters.
# Example: aaabbccccd -> a3b2c4d1

s = input("Enter a string: ")

if not s:
    print("Compressed string: ")

else:
    compressed = ""
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed += s[i - 1] + str(count)
            count = 1
    compressed += s[-1] + str(count)

    print(f"Compressed string: {compressed}")