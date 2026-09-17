# 10.	Create an abstract class Appointment with abstract methods book_appointment() and calculate_fee(). Derive GeneralAppointment, SpecialistAppointment, and EmergencyAppointment.

from abc import ABC, abstractmethod

class Appointment(ABC):
    def __init__(self, patient_name, doctor_name):
        self.patient_name = patient_name
        self.doctor_name = doctor_name

    @abstractmethod
    def book_appointment(self, slot_time):
        pass

    @abstractmethod
    def calculate_fee(self):
        pass


class GeneralAppointment(Appointment):
    def book_appointment(self, slot_time):
        print(f"[General Consultation] Booked for {self.patient_name} with Dr. {self.doctor_name} at {slot_time}.")

    def calculate_fee(self):
        return 500.0


class SpecialistAppointment(Appointment):
    def __init__(self, patient_name, doctor_name, specialty):
        super().__init__(patient_name, doctor_name)
        self.specialty = specialty

    def book_appointment(self, slot_time):
        print(f"[Specialist Consultation: {self.specialty}] Reserved for {self.patient_name} with Dr. {self.doctor_name} at {slot_time}.")

    def calculate_fee(self):
        return 1500.0


class EmergencyAppointment(Appointment):
    def book_appointment(self, slot_time):
        print(f"[EMERGENCY APPOINTMENT] IMMEDIATE PRIORITY TRIAGE assigned for {self.patient_name} under ER Lead Dr. {self.doctor_name} at {slot_time}!")

    def calculate_fee(self):
        return 3500.0


appointments = [
    (GeneralAppointment("Suresh Patel", "R. K. Sen"), "10:30 AM"),
    (SpecialistAppointment("Meena Gupta", "A. V. Rao", "Neurology"), "02:15 PM"),
    (EmergencyAppointment("Rohan Verma", "K. L. Sharma"), "NOW (04:10 PM)")
]

print("Hospital Appointment Scheduling System")
for appt, time_slot in appointments:
    appt.book_appointment(time_slot)
    print(f"Consultation Fee: Rs. {appt.calculate_fee():.2f}\n")
