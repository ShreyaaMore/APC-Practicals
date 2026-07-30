# Write a PYTHON program to produce following design
#       A
#       A B
#       A B C
#       A B C D 
#       A B C D E
#       If user enters n value as 5

n = int(input("Enter a number: "))
alphas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

if n <= 26:
    for i in range(1, n+1):
        for j in range(i):
            print(alphas[j], end=" ")
        print()
else:
    print("Invalid")
