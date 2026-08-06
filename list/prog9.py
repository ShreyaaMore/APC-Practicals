# 9.	Create a list of cities. Ask the user to enter a city name and check whether it exists in the list.

cities = ["Kolhapur", "Mumbai", "Pune", "Sangli", "Satara"]

print("Cities:",cities)

c = input("Enter a city to check if it exists in list: ").capitalize()

if c in cities:
    print("City is in the list.")
else:
    print("City is not in the list.")
    