# 14.	Create classes Camera and Phone. The Camera class should provide methods for taking photographs, while Phone should provide methods for making calls. Create a Smartphone class inheriting from both.

class Camera:
    def __init__(self, megapixels):
        self.megapixels = megapixels

    def take_photo(self):
        print(f"[Camera] Capturing high-resolution photo with {self.megapixels} MP sensor.")


class Phone:
    def __init__(self, phone_number):
        self.phone_number = phone_number

    def make_call(self, contact_number):
        print(f"[Phone] Dialing {contact_number} from {self.phone_number}...")


class Smartphone(Camera, Phone):
    def __init__(self, brand, model, megapixels, phone_number, os_name):
        Camera.__init__(self, megapixels)
        Phone.__init__(self, phone_number)
        self.brand = brand
        self.model = model
        self.os_name = os_name

    def display_device(self):
        print(f"Device : {self.brand} {self.model} (OS: {self.os_name})")
        print(f"Camera : {self.megapixels} MP")
        print(f"SIM No : {self.phone_number}\n")


sp = Smartphone("Google", "Pixel 8 Pro", 50, "+91-9876543210", "Android 15")
print("Smartphone Functionality")
sp.display_device()
sp.make_call("+91-9123456780")
sp.take_photo()
