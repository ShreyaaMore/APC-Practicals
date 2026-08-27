# Define a function that accepts two numbers and returns the greater number

def greater(a, b):
    if a>b:
        return(a)
    else:
        return(b)

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

print(greater(a, b))