"""Medical records module."""

def create_medical_record(record_id, patient_id, doctor_id, diagnosis, treatment):
    return {
        "record_id": record_id,
        "patient_id": patient_id,
        "doctor_id": doctor_id,
        "diagnosis": diagnosis,
        "treatment": treatment
    }

