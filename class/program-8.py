# 8.	Create a class Patient containing patient ID, name, age, disease, and consultation fee. Define methods to display patient information and calculate the total bill.

class Patient:
    def __init__(self, patient_id, name, age, disease, consultation_fee):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease
        self.consultation_fee = consultation_fee

    def display_info(self):
        print(f"Patient ID       : {self.patient_id}")
        print(f"Name             : {self.name}")
        print(f"Age              : {self.age}")
        print(f"Disease          : {self.disease}")
        print(f"Consultation Fee : Rs. {self.consultation_fee:.2f}")

    def calculate_total_bill(self, medicine_charges=0.0, test_charges=0.0):
        total = self.consultation_fee + medicine_charges + test_charges
        return total


p = Patient("P201", "Kavita Joshi", 45, "Viral Fever", 500.0)
print("Patient Details")
p.display_info()
total = p.calculate_total_bill(medicine_charges=750.0, test_charges=1200.0)
print(f"Total Bill (Consultation + Medicines + Tests): Rs. {total:.2f}")
