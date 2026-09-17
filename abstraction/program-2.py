# 2.	Create an abstract class Vehicle with abstract methods start() and stop(). Derive Car, Bike, and Bus classes and implement these methods.

from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, model):
        self.model = model

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def start(self):
        print(f"Car [{self.model}]: Key turned, engine started smoothly.")

    def stop(self):
        print(f"Car [{self.model}]: Disc brakes engaged, engine switched off.")


class Bike(Vehicle):
    def start(self):
        print(f"Bike [{self.model}]: Kick-started, headlights on.")

    def stop(self):
        print(f"Bike [{self.model}]: Handbrake pulled, side-stand deployed.")


class Bus(Vehicle):
    def start(self):
        print(f"Bus [{self.model}]: Air pressure built up, ignition turned on.")

    def stop(self):
        print(f"Bus [{self.model}]: Air brakes applied, passenger doors open.")


fleet = [
    Car("Maruti Swift"),
    Bike("Royal Enfield Hunter"),
    Bus("Tata Starbus")
]

print("Vehicle Operations via Abstraction")
for v in fleet:
    v.start()
    v.stop()
    print("-" * 35)
