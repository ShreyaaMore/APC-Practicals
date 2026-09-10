# 10.	Create a class Vehicle containing vehicle number, model, rental rate, and availability. Implement methods to rent and return a vehicle and calculate rental charges based on the number of days.

class Vehicle:
    def __init__(self, vehicle_no, model, rental_rate_per_day, availability=True):
        self.vehicle_no = vehicle_no
        self.model = model
        self.rental_rate_per_day = rental_rate_per_day
        self.availability = availability

    def rent_vehicle(self, days):
        if not self.availability:
            print(f"Sorry, {self.model} ({self.vehicle_no}) is currently not available.")
            return 0.0
        self.availability = False
        charges = days * self.rental_rate_per_day
        print(f"{self.model} ({self.vehicle_no}) rented for {days} days.")
        print(f"Rental charges: Rs. {charges:.2f}")
        return charges

    def return_vehicle(self):
        if self.availability:
            print(f"{self.model} ({self.vehicle_no}) is already available.")
        else:
            self.availability = True
            print(f"{self.model} ({self.vehicle_no}) has been returned successfully.")

    def display_status(self):
        status = "Available" if self.availability else "Rented"
        print(f"Vehicle: {self.model} [{self.vehicle_no}], Rate: Rs. {self.rental_rate_per_day}/day, Status: {status}")


v1 = Vehicle("MH-12-AB-1234", "Honda City", 2000.0)
v1.display_status()
v1.rent_vehicle(4)
v1.display_status()
v1.rent_vehicle(2)
v1.return_vehicle()
v1.display_status()
