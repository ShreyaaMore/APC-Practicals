# Create a function simple_interest(p, r, t) to calculate simple interest

def simple_interest(p, r, t):
    si = (p*r*t)/100
    return si


p = int(input("Enter principal amount: "))
r = int(input("Enter rate of interest: "))
t = int(input("Enter time period: "))

print("Simple Interest:",simple_interest(p, r, t))