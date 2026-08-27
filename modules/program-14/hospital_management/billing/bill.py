"""Hospital billing module."""

def calculate_hospital_bill(consultation_fee, test_charges, medicine_charges, room_charges=0.0):
    total = consultation_fee + test_charges + medicine_charges + room_charges
    return {
        "consultation": consultation_fee,
        "tests": test_charges,
        "medicines": medicine_charges,
        "room": room_charges,
        "total": total
    }

