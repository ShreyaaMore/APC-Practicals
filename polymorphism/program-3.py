# 3.	Create a base class Vehicle with a method start(). Derive Car, Bike, and Bus classes and override start() to display the starting behavior of each vehicle.

class Vehicle:
    def __init__(self, model):
        self.model = model

    def start(self):
        print(f"{self.model} vehicle is starting.")


class Car(Vehicle):
    def start(self):
        print(f"Car [{self.model}]: Push button start engaged. Engine purrs smoothly.")


class Bike(Vehicle):
    def start(self):
        print(f"Bike [{self.model}]: Self-start switch pressed. Throttle ready to rev.")


class Bus(Vehicle):
    def start(self):
        print(f"Bus [{self.model}]: Pneumatic air brakes released, heavy diesel ignition started.")


vehicles = [
    Car("Honda Civic"),
    Bike("Yamaha MT-15"),
    Bus("Volvo 9400 B11R")
]

print("Starting Vehicles (Polymorphism)")
for v in vehicles:
    v.start()
