# 10.	Create a Pandas Series using a dictionary containing product names and prices.
# Perform:
# •	Display all products and prices. 
# •	Increase every price by 10%. 
# •	Find the most expensive product. 
# •	Find products costing more than ₹1,000.

import pandas as pd

product_prices = {
    "Keyboard": 1500,
    "Mouse": 650,
    "USB Flash Drive": 450,
    "External Hard Drive": 4200,
    "HDMI Cable": 350,
    "Gaming Headset": 2800
}

prices = pd.Series(product_prices)

print("1. All Products and Prices")
print(prices)

increased_prices = prices * 1.10
print("\n2. Prices After 10% Increase")
print(increased_prices.round(2))

print(f"\n3. Most Expensive Product: {prices.idxmax()} (₹{prices.max()})")

print("\n4. Products Costing More Than ₹1,000")
print(prices[prices > 1000])

