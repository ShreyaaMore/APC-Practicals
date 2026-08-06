# Accept 10 numbers from the user and store them in a list. Calculate:
# •	Sum 
# •	Average 

l = []

for i in range(10):
    num = int(input("Enter number: "))
    l.append(num)

print("List: ", l)

print("The sum is:", sum(l))

print("The average is:", sum(l)/len(l))
