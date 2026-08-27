# Write a function that accepts a list of numbers and returns the largest element without using the built-in max() function

def largest(l):
    max = l[0]
    for i in l:
        if i>max:
            max = i

    return max

l = [10,35,42,65,75,86,25,19,74]
print("Largest element:",largest(l))