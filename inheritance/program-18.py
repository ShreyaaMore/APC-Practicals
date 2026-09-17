# 18.	Create a class Person and derive Doctor and Patient. Create additional classes representing Surgeon and MedicalResearcher. Design the hierarchy so that the program demonstrates multiple inheritance along with hierarchical inheritance.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print(f"Name : {self.name} | Age: {self.age}")


class Doctor(Person):
    def __init__(self, name, age, doctor_id, specialization):
        super().__init__(name, age)
        self.doctor_id = doctor_id
        self.specialization = specialization

    def display_doctor(self):
        self.display_person()
        print(f"Doctor ID      : {self.doctor_id}")
        print(f"Specialization : {self.specialization}")


class Patient(Person):
    def __init__(self, name, age, patient_id, ailment):
        super().__init__(name, age)
        self.patient_id = patient_id
        self.ailment = ailment

    def display_patient(self):
        print("Patient Details")
        self.display_person()
        print(f"Patient ID : {self.patient_id}")
        print(f"Ailment    : {self.ailment}\n")


class Surgeon(Doctor):
    def __init__(self, name, age, doctor_id, specialization, surgeries_performed):
        super().__init__(name, age, doctor_id, specialization)
        self.surgeries_performed = surgeries_performed

    def perform_surgery(self):
        print(f"Dr. {self.name} has performed {self.surgeries_performed} major surgeries.")


class MedicalResearcher(Doctor):
    def __init__(self, name, age, doctor_id, specialization, research_lab, clinical_trials):
        super().__init__(name, age, doctor_id, specialization)
        self.research_lab = research_lab
        self.clinical_trials = clinical_trials

    def conduct_trial(self):
        print(f"Dr. {self.name} is directing {self.clinical_trials} clinical trials at {self.research_lab}.")


class SurgeonResearcher(Surgeon, MedicalResearcher):
    def __init__(self, name, age, doctor_id, specialization, surgeries_performed, research_lab, clinical_trials):
        Surgeon.__init__(self, name, age, doctor_id, specialization, surgeries_performed)
        MedicalResearcher.__init__(self, name, age, doctor_id, specialization, research_lab, clinical_trials)

    def display_profile(self):
        print("Surgeon & Medical Researcher Profile (Hybrid Inheritance)")
        self.display_doctor()
        self.perform_surgery()
        self.conduct_trial()
        print()


pat = Patient("Vikram Singhania", 52, "P-104", "Coronary Artery Disease")
pat.display_patient()

sr = SurgeonResearcher("Ananya Kulkarni", 42, "DOC-701", "Cardiothoracic Surgery", 320, "Apex Cardiac Genomics Lab", 3)
sr.display_profile()
