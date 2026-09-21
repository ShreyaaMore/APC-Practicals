# 5.	Create a dictionary containing:
# Order_ID
# Customer
# Product
# Quantity
# Price
# Discount
# Create a DataFrame and calculate:
# Final Amount = Quantity × Price − Discount
# Then display:
# •	All orders 
# •	Orders above ₹5,000 
# •	Highest-value order 
# •	Average order value

import pandas as pd

data = {
    "Order_ID": ["ORD01", "ORD02", "ORD03", "ORD04", "ORD05"],
    "Customer": ["Meera", "Karan", "Tanvi", "Siddharth", "Zoya"],
    "Product": ["Tablet", "Headphones", "Smartwatch", "Monitor", "Power Bank"],
    "Quantity": [1, 3, 2, 1, 4],
    "Price": [18000, 2500, 4500, 12000, 1200],
    "Discount": [1000, 500, 600, 1200, 300]
}

df = pd.DataFrame(data)

df["Final_Amount"] = (df["Quantity"] * df["Price"]) - df["Discount"]

print("All Orders")
print(df)

print("\nOrders Above ₹5,000")
print(df[df["Final_Amount"] > 5000])

highest_order = df.loc[df["Final_Amount"].idxmax()]
print("\nHighest-Value Order")
print(f"Order ID     : {highest_order['Order_ID']}")
print(f"Customer     : {highest_order['Customer']}")
print(f"Product      : {highest_order['Product']}")
print(f"Final Amount : ₹{highest_order['Final_Amount']:,.2f}")

avg_order = df["Final_Amount"].mean()
print(f"\nAverage Order Value: ₹{avg_order:,.2f}")

