# 15.	Create a base class SmartDevice with methods turn_on() and turn_off(). Derive Light, Fan, AC, and TV. Override the methods according to each device.

class SmartDevice:
    def __init__(self, room):
        self.room = room
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print(f"Device in {self.room} is now turned ON.")

    def turn_off(self):
        self.is_on = False
        print(f"Device in {self.room} is now turned OFF.")


class Light(SmartDevice):
    def __init__(self, room, brightness=100):
        super().__init__(room)
        self.brightness = brightness

    def turn_on(self):
        self.is_on = True
        print(f"[Smart Light] {self.room}: Illuminated with Warm White at {self.brightness}% brightness.")

    def turn_off(self):
        self.is_on = False
        print(f"[Smart Light] {self.room}: Bulb dimmed and switched OFF.")


class Fan(SmartDevice):
    def __init__(self, room, speed=3):
        super().__init__(room)
        self.speed = speed

    def turn_on(self):
        self.is_on = True
        print(f"[Smart Fan] {self.room}: Spinning at speed level {self.speed}.")

    def turn_off(self):
        self.is_on = False
        print(f"[Smart Fan] {self.room}: Motor halted.")


class AC(SmartDevice):
    def __init__(self, room, temp_c=24):
        super().__init__(room)
        self.temp_c = temp_c

    def turn_on(self):
        self.is_on = True
        print(f"[Smart AC] {self.room}: Inverter compressor active, cooling to {self.temp_c}°C.")

    def turn_off(self):
        self.is_on = False
        print(f"[Smart AC] {self.room}: Louvers closed, standby mode.")


class TV(SmartDevice):
    def __init__(self, room, channel="Netflix"):
        super().__init__(room)
        self.channel = channel

    def turn_on(self):
        self.is_on = True
        print(f"[Smart TV] {self.room}: OLED display ON, opening app '{self.channel}'.")

    def turn_off(self):
        self.is_on = False
        print(f"[Smart TV] {self.room}: Display powered OFF.")


devices = [
    Light("Living Room", 80),
    Fan("Master Bedroom", 4),
    AC("Home Office", 22),
    TV("Living Room", "YouTube")
]

print("=== Activating Smart Home Scene ===")
for dev in devices:
    dev.turn_on()

print("\n=== Power Saving / Leaving Home Scene ===")
for dev in devices:
    dev.turn_off()
