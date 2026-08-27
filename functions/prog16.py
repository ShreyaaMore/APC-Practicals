# Create a function to find the second-largest number in a list.

def largest(l):
    l.sort()
    return(l[-2])

l = [10,35,42,65,75,86,25,19,74]
print("Second Largest element:",largest(l))