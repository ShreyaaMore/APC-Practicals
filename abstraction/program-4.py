# 4.	Create an abstract class FoodOrder with abstract methods calculate_bill() and delivery_charge(). Derive RestaurantOrder and HomeDeliveryOrder and implement the methods appropriately.

from abc import ABC, abstractmethod

class FoodOrder(ABC):
    def __init__(self, order_id, items):
        self.order_id = order_id
        self.items = items

    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def delivery_charge(self):
        pass

    def get_items_total(self):
        return sum(self.items.values())


class RestaurantOrder(FoodOrder):
    def __init__(self, order_id, items, table_no, service_charge_pct=5.0):
        super().__init__(order_id, items)
        self.table_no = table_no
        self.service_charge_pct = service_charge_pct

    def delivery_charge(self):
        return 0.0

    def calculate_bill(self):
        subtotal = self.get_items_total()
        service_charge = subtotal * (self.service_charge_pct / 100)
        return subtotal + service_charge + self.delivery_charge()


class HomeDeliveryOrder(FoodOrder):
    def __init__(self, order_id, items, distance_km, address):
        super().__init__(order_id, items)
        self.distance_km = distance_km
        self.address = address

    def delivery_charge(self):
        if self.distance_km <= 2:
            return 30.0
        return 30.0 + (self.distance_km - 2) * 10.0

    def calculate_bill(self):
        subtotal = self.get_items_total()
        tax = subtotal * 0.05
        return subtotal + tax + self.delivery_charge()


items = {"Paneer Tikka": 280.0, "Garlic Naan": 90.0, "Biryani": 320.0}

dine_in = RestaurantOrder("ORD-101", items, table_no=5)
delivery = HomeDeliveryOrder("ORD-102", items, distance_km=5.5, address="402 Green View Apts")

print("Restaurant Dine-In Order")
print(f"Table No        : {dine_in.table_no}")
print(f"Items Subtotal  : Rs. {dine_in.get_items_total():.2f}")
print(f"Delivery Charge : Rs. {dine_in.delivery_charge():.2f}")
print(f"Total Bill      : Rs. {dine_in.calculate_bill():.2f}\n")

print("Home Delivery Order")
print(f"Delivery Address: {delivery.address}")
print(f"Distance        : {delivery.distance_km} km")
print(f"Delivery Charge : Rs. {delivery.delivery_charge():.2f}")
print(f"Total Bill      : Rs. {delivery.calculate_bill():.2f}")
