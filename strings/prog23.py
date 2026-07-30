# Compress repeated characters and return the original string if compression does not reduce the length.

s = input("Enter a string: ")

if not s:
    print("Result: ")
else:
    compressed_parts = []
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed_parts.append(s[i - 1] + str(count))
            count = 1
            
    compressed_parts.append(s[-1] + str(count))

    compressed = "".join(compressed_parts)

    if len(compressed) < len(s):
        print(f"Compressed string: {compressed}")
    else:
        print(f"Original string (compression did not reduce length): {s}")