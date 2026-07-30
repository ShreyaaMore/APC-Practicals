# Check whether one string is a rotation of another.

s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")

if len(s1) != len(s2) or len(s1) == 0:
    print("They are NOT rotations of each other.")
else:
    doubled_string = s1 + s1
    
    if s2 in doubled_string:
        print(f"Yes, {s2} is a rotation of {s1}.")
    else:
        print("They are NOT rotations of each other.")