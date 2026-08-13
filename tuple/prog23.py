# Store item prices in a tuple and calculate:
# •	Total bill 
# •	Average price 
# •	Highest-priced item 
# •	Lowest-priced item

items = (150,250,300,450,100,200,350,400)

print(f"The total bill is {sum(items)}")
print(f"The average price is {sum(items)/len(items)}")
print(f"The Highest price is {max(items)}")
print(f"The Lowest price is {min(items)}")