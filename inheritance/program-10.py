# 10.	Create a base class Vehicle. Derive Car and Bike from Vehicle. Create a class SportsCar that inherits from Car and another class ElectricBike that inherits from Bike. Add suitable attributes and methods to demonstrate a combination of inheritance types.

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_vehicle(self):
        print(f"Brand : {self.brand}")
        print(f"Model : {self.model}")


class Car(Vehicle):
    def __init__(self, brand, model, seating_capacity):
        super().__init__(brand, model)
        self.seating_capacity = seating_capacity

    def display_car(self):
        self.display_vehicle()
        print(f"Seating Capacity : {self.seating_capacity} passengers")


class Bike(Vehicle):
    def __init__(self, brand, model, engine_cc):
        super().__init__(brand, model)
        self.engine_cc = engine_cc

    def display_bike(self):
        self.display_vehicle()
        print(f"Engine Capacity  : {self.engine_cc} cc")


class SportsCar(Car):
    def __init__(self, brand, model, seating_capacity, top_speed, turbo_mode):
        super().__init__(brand, model, seating_capacity)
        self.top_speed = top_speed
        self.turbo_mode = turbo_mode

    def display_sports_car(self):
        print("Sports Car Details")
        self.display_car()
        print(f"Top Speed        : {self.top_speed} km/h")
        print(f"Turbo Mode       : {'Available' if self.turbo_mode else 'No'}\n")


class ElectricBike(Bike):
    def __init__(self, brand, model, engine_cc, battery_capacity, range_km):
        super().__init__(brand, model, engine_cc)
        self.battery_capacity = battery_capacity
        self.range_km = range_km

    def display_electric_bike(self):
        print("Electric Bike Details")
        self.display_bike()
        print(f"Battery Capacity : {self.battery_capacity} kWh")
        print(f"Riding Range     : {self.range_km} km per charge\n")


sc = SportsCar("Ferrari", "488 Pista", 2, 340, True)
eb = ElectricBike("Revolt", "RV400", 0, 3.24, 150)

sc.display_sports_car()
eb.display_electric_bike()
