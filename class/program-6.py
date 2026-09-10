# 6.	Create a class ElectricityBill containing consumer number, consumer name, and units consumed. Define a method to calculate the electricity bill according to different unit slabs.

class ElectricityBill:
    def __init__(self, consumer_no, consumer_name, units_consumed):
        self.consumer_no = consumer_no
        self.consumer_name = consumer_name
        self.units_consumed = units_consumed

    def calculate_bill(self):
        units = self.units_consumed
        bill = 50.0

        if units <= 100:
            bill += units * 3.0
        elif units <= 200:
            bill += (100 * 3.0) + (units - 100) * 4.5
        elif units <= 300:
            bill += (100 * 3.0) + (100 * 4.5) + (units - 200) * 6.0
        else:
            bill += (100 * 3.0) + (100 * 4.5) + (100 * 6.0) + (units - 300) * 8.0

        return bill

    def display_bill(self):
        print(f"Consumer Number : {self.consumer_no}")
        print(f"Consumer Name   : {self.consumer_name}")
        print(f"Units Consumed  : {self.units_consumed}")
        print(f"Total Bill      : Rs. {self.calculate_bill():.2f}\n")


eb1 = ElectricityBill("C1001", "Sneha Roy", 85)
eb2 = ElectricityBill("C1002", "Vikram Rathore", 240)

print("Electricity Bills")
eb1.display_bill()
eb2.display_bill()
