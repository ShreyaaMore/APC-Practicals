# Store temperatures of seven days in a tuple and determine:
# •	Maximum temperature 
# •	Minimum temperature 
# •	Average temperature 

temperatures = (25,32,34,36,22,29,30,26,28)

print(f"The Maximum Temperature is {max(temperatures)}")
print(f"The Minimum Temperature is {min(temperatures)}")
print(f"The Average Temperature is {sum(temperatures)/len(temperatures)}")
