# Write a function that accepts a list of numbers and returns their average

def average(l):
    return(sum(l)/len(l))

l = [34,52,41,16,35,75,49,25]
print("Average is",average(l))