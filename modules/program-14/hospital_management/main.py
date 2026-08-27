# 14.	Create a project directory containing packages for:
# a)	Patient management 
# b)	Doctor management 
# c)	Billing 
# d)	Medical records 
# Implement simple functions in each module and access them from main.py.

from patient_management.patient import register_patient
from doctor_management.doctor import get_doctor
from billing.bill import calculate_hospital_bill
from medical_records.record import create_medical_record

print("Hospital Management System:\n")

patient = register_patient("P001", "Rohan Mehta", 34, "Male")
print(f"Patient Registered : {patient['name']} (ID: {patient['patient_id']}, Age: {patient['age']})")

doctor = get_doctor("DOC105", "Dr. Shalini Deshmukh", "Cardiology", "+91-9876543210")
print(f"Assigned Doctor    : {doctor['name']} ({doctor['department']})")

record = create_medical_record("REC901", patient["patient_id"], doctor["doctor_id"], "Mild Hypertension", "Prescribed Beta-blockers and lifestyle changes")
print(f"\nMedical Record [{record['record_id']}]:")
print(f" - Diagnosis : {record['diagnosis']}")
print(f" - Treatment : {record['treatment']}")

bill = calculate_hospital_bill(consultation_fee=800.0, test_charges=1500.0, medicine_charges=650.0)
print("\nHospital Bill:")
print(f"Consultation Fee : Rs. {bill['consultation']:.2f}")
print(f"Test Charges     : Rs. {bill['tests']:.2f}")
print(f"Medicine Charges : Rs. {bill['medicines']:.2f}")
print(f"Total Amount Due : Rs. {bill['total']:.2f}")

