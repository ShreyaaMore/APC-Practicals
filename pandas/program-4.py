# 4.	Create a dictionary containing:
# Patient ID
# Patient Name
# Age
# Disease
# Medical Charges
# Convert the dictionary into a DataFrame and:
# 1.	Display patients above 60 years. 
# 2.	Find the average medical charge. 
# 3.	Find the maximum medical charge. 
# 4.	Display patients whose medical charges are greater than ₹50,000. 

import pandas as pd

data = {
    "Patient_ID": ["P101", "P102", "P103", "P104", "P105"],
    "Patient_Name": ["Ramesh", "Sunita", "Kishore", "Anjali", "Omkar"],
    "Age": [65, 45, 72, 28, 68],
    "Disease": ["Diabetes", "Hypertension", "Cardiac", "Asthma", "Cardiac"],
    "Medical_Charges": [45000, 32000, 85000, 15000, 92000]
}

df = pd.DataFrame(data)

print("Patients DataFrame")
print(df)

print("\n1. Patients Above 60 Years")
print(df[df["Age"] > 60])

avg_charge = df["Medical_Charges"].mean()
print(f"\n2. Average Medical Charge: ₹{avg_charge:,.2f}")

max_charge = df["Medical_Charges"].max()
print(f"\n3. Maximum Medical Charge: ₹{max_charge:,.2f}")

print("\n4. Patients with Medical Charges > ₹50,000")
print(df[df["Medical_Charges"] > 50000])

