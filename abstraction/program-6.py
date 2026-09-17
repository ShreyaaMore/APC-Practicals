# 6.	Create an abstract class Transport with an abstract method calculate_fare(distance). Implement subclasses:
# a)	Bus 
# b)	Train 
# c)	Taxi 
# d)	Flight 
# Calculate the fare according to the transportation type.

from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def calculate_fare(self, distance):
        pass


class Bus(Transport):
    def calculate_fare(self, distance):
        return max(15.0, distance * 2.5)


class Train(Transport):
    def calculate_fare(self, distance):
        return max(50.0, distance * 1.2)


class Taxi(Transport):
    def calculate_fare(self, distance):
        return 50.0 + (distance * 15.0)


class Flight(Transport):
    def calculate_fare(self, distance):
        return 2500.0 + (distance * 5.5)


distance_km = 350
transports = {
    "Bus": Bus(),
    "Train": Train(),
    "Taxi": Taxi(),
    "Flight": Flight()
}

print(f"Fare Estimation for Distance: {distance_km} km")
for mode, transport in transports.items():
    fare = transport.calculate_fare(distance_km)
    print(f"Mode: {mode:<8} | Fare: Rs. {fare:.2f}")
