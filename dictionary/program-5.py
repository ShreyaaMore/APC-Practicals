# 5.	Create a dictionary of cities and their populations. Remove a specified city from the dictionary.

cities = {
    "Amravati": 48945498,
    "Kolhapur": 34844684,
    "Akola": 498454,
    "Yavatmal": 48948645,
    "Pune": 958465545,
    "Mumbai": 1845745784
}


print("Cities Population:", cities)

city_rm = input("Enter city name to remove it: ")

if city_rm in cities:
    cities.pop(city_rm)
    print("\nCities Population:", cities)
else:
    print("No such City.")