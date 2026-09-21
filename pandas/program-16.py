# 16.	Dataset: weather.csv
# Columns:
# Date,City,Temperature,Humidity,Rainfall
# Problem Statement:
# Read the CSV file and:
# 1.	Find the maximum temperature. 
# 2.	Find the minimum temperature. 
# 3.	Calculate the average temperature. 
# 4.	Display records where temperature is above 35°C. 
# 5.	Calculate city-wise average temperature.

import os
import pandas as pd

csv_path = os.path.join(os.path.dirname(__file__), "weather.csv")
df = pd.read_csv(csv_path)

print("Weather Dataset")
print(df)

print(f"\n1. Maximum Temperature: {df['Temperature'].max()}°C")

print(f"2. Minimum Temperature: {df['Temperature'].min()}°C")

print(f"3. Average Temperature: {df['Temperature'].mean():.2f}°C")

print("\n4. Weather Records Where Temperature > 35°C")
print(df[df["Temperature"] > 35.0])

print("\n5. City-wise Average Temperature")
city_avg = df.groupby("City")["Temperature"].mean()
print(city_avg.round(2))

