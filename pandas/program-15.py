# 15.	Dataset: patients.csv
# Columns:
# Patient_ID,Name,Age,Gender,Disease,Medical_Expense
# Problem Statement:
# Read the CSV file and:
# 1.	Display patients above 60 years. 
# 2.	Calculate average medical expense. 
# 3.	Find the patient with the highest medical expense. 
# 4.	Count patients for each disease. 
# 5.	Display patients whose medical expense exceeds ₹50,000.

import os
import pandas as pd

csv_path = os.path.join(os.path.dirname(__file__), "patients.csv")
df = pd.read_csv(csv_path)

print("Patients Dataset")
print(df)

print("\n1. Patients Above 60 Years")
print(df[df["Age"] > 60])

print(f"\n2. Average Medical Expense: ₹{df['Medical_Expense'].mean():,.2f}")

max_exp_patient = df.loc[df["Medical_Expense"].idxmax()]
print("\n3. Patient with Highest Medical Expense")
print(f"Name    : {max_exp_patient['Name']} [{max_exp_patient['Patient_ID']}]")
print(f"Expense : ₹{max_exp_patient['Medical_Expense']:,d} ({max_exp_patient['Disease']})")

print("\n4. Patient Count by Disease")
print(df["Disease"].value_counts())

print("\n5. Patients with Expense > ₹50,000")
print(df[df["Medical_Expense"] > 50000])

