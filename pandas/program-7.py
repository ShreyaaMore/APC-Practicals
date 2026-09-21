# 7.	A retail shop maintains sales information in a Python dictionary containing Product_ID, Product_Name, Category, Price, and Quantity.
# Write a Python program to:
# 1.	Convert the dictionary into a Pandas DataFrame. 
# 2.	Add a new column Total_Sales. 
# 3.	Calculate the total sales using Price × Quantity. 
# 4.	Display products with sales greater than ₹10,000. 
# 5.	Find the product with maximum sales. 
# 6.	Calculate the average sales.

import pandas as pd

retail_data = {
    "Product_ID": ["RT101", "RT102", "RT103", "RT104", "RT105"],
    "Product_Name": ["Office Chair", "Desk Lamp", "Ergonomic Desk", "Wireless Mouse", "Webcam"],
    "Category": ["Furniture", "Lighting", "Furniture", "Accessories", "Electronics"],
    "Price": [7500, 1200, 18000, 650, 3200],
    "Quantity": [3, 8, 2, 15, 5]
}

df = pd.DataFrame(retail_data)

df["Total_Sales"] = df["Price"] * df["Quantity"]

print("Retail Sales DataFrame")
print(df)

print("\nProducts with Sales > ₹10,000")
print(df[df["Total_Sales"] > 10000])

max_sale_prod = df.loc[df["Total_Sales"].idxmax()]
print("\nProduct with Maximum Sales")
print(f"Name        : {max_sale_prod['Product_Name']}")
print(f"Total Sales : ₹{max_sale_prod['Total_Sales']:,.2f}")

avg_sales = df["Total_Sales"].mean()
print(f"\nAverage Sales: ₹{avg_sales:,.2f}")

