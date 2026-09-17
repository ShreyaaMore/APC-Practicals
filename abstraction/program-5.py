# 5.	Create an abstract class Patient with abstract methods calculate_bill() and treatment(). Derive InPatient, OutPatient, and EmergencyPatient classes and implement the methods according to the patient type.

from abc import ABC, abstractmethod

class Patient(ABC):
    def __init__(self, patient_id, name):
        self.patient_id = patient_id
        self.name = name

    @abstractmethod
    def treatment(self):
        pass

    @abstractmethod
    def calculate_bill(self):
        pass

    def display_basic(self):
        print(f"Patient ID: {self.patient_id} | Name: {self.name}")


class InPatient(Patient):
    def __init__(self, patient_id, name, days_admitted, room_rate=2500.0, medicine_cost=4000.0):
        super().__init__(patient_id, name)
        self.days_admitted = days_admitted
        self.room_rate = room_rate
        self.medicine_cost = medicine_cost

    def treatment(self):
        print(f"[In-Patient] {self.name}: Admitted for {self.days_admitted} days with continuous IV monitoring and physician rounds.")

    def calculate_bill(self):
        return (self.days_admitted * self.room_rate) + self.medicine_cost


class OutPatient(Patient):
    def __init__(self, patient_id, name, consultation_fee=800.0, lab_fee=650.0):
        super().__init__(patient_id, name)
        self.consultation_fee = consultation_fee
        self.lab_fee = lab_fee

    def treatment(self):
        print(f"[Out-Patient] {self.name}: General clinical OPD checkup and diagnostic blood tests.")

    def calculate_bill(self):
        return self.consultation_fee + self.lab_fee


class EmergencyPatient(Patient):
    def __init__(self, patient_id, name, trauma_care_fee=5000.0, surgery_cost=18000.0):
        super().__init__(patient_id, name)
        self.trauma_care_fee = trauma_care_fee
        self.surgery_cost = surgery_cost

    def treatment(self):
        print(f"[Emergency] {self.name}: Immediate ICU stabilization, oxygen support, and emergency surgical intervention.")

    def calculate_bill(self):
        return self.trauma_care_fee + self.surgery_cost


patients = [
    InPatient("IN-201", "Mahesh Kadam", days_admitted=4),
    OutPatient("OUT-305", "Pooja Hegde"),
    EmergencyPatient("EM-009", "Vikram Rathore")
]

print("Patient Hospital Records via Abstraction")
for p in patients:
    p.display_basic()
    p.treatment()
    print(f"Total Bill: Rs. {p.calculate_bill():.2f}")
    print("-" * 45)
