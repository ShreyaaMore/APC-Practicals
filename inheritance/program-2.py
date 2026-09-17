# 2.	Create a base class Vehicle with attributes brand and model. Create a derived class Car with additional attributes fuel_type and price. Define methods to display vehicle details and calculate the discounted price of the car.

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_vehicle(self):
        print(f"Brand : {self.brand}")
        print(f"Model : {self.model}")


class Car(Vehicle):
    def __init__(self, brand, model, fuel_type, price):
        super().__init__(brand, model)
        self.fuel_type = fuel_type
        self.price = price

    def calculate_discounted_price(self, discount_percent):
        return self.price - (self.price * (discount_percent / 100))

    def display_car_details(self, discount_percent=0.0):
        self.display_vehicle()
        print(f"Fuel Type        : {self.fuel_type}")
        print(f"Original Price   : Rs. {self.price:.2f}")
        if discount_percent > 0:
            discounted = self.calculate_discounted_price(discount_percent)
            print(f"Discounted ({discount_percent}%) : Rs. {discounted:.2f}")
        print()


c = Car("Hyundai", "Creta", "Diesel", 1600000.0)
print("Car Details")
c.display_car_details(discount_percent=7.5)
