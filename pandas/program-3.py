# 3.	Create a dictionary containing:
# Product ID
# Product Name
# Category
# Price
# Quantity
# Convert it into a DataFrame.
# Calculate:
# Total Amount = Price × Quantity
# Then find the product having the highest total sales.

import pandas as pd

data = {
    "Product_ID": ["P01", "P02", "P03", "P04", "P05"],
    "Product_Name": ["Laptop", "Mouse", "Monitor", "Keyboard", "Headphones"],
    "Category": ["Electronics", "Accessories", "Electronics", "Accessories", "Audio"],
    "Price": [55000, 800, 14000, 2500, 3500],
    "Quantity": [4, 25, 6, 12, 10]
}

df = pd.DataFrame(data)

df["Total_Amount"] = df["Price"] * df["Quantity"]

print("Product Sales DataFrame")
print(df)

highest_sale_prod = df.loc[df["Total_Amount"].idxmax()]
print("\nProduct with Highest Total Sales")
print(f"Product Name : {highest_sale_prod['Product_Name']} [{highest_sale_prod['Product_ID']}]")
print(f"Total Sales  : ₹{highest_sale_prod['Total_Amount']:,.2f}")

