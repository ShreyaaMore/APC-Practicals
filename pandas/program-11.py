# 11.	Create a Pandas Series using a dictionary where patient IDs are the index and patient ages are the values.
# Perform:
# •	Find the average age. 
# •	Find the oldest patient. 
# •	Find the youngest patient. 
# •	Display patients above 60 years.

import pandas as pd

patient_ages = {
    "PID_101": 45,
    "PID_102": 68,
    "PID_103": 29,
    "PID_104": 74,
    "PID_105": 52,
    "PID_106": 81,
    "PID_107": 36
}

ages = pd.Series(patient_ages)

print("Patient Ages Series")
print(ages)

print(f"\nAverage Age      : {ages.mean():.1f} years")

print(f"Oldest Patient   : {ages.idxmax()} ({ages.max()} years)")

print(f"Youngest Patient : {ages.idxmin()} ({ages.min()} years)")

print("\nPatients Above 60 Years")
print(ages[ages > 60])

