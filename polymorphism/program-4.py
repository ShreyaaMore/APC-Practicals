# 4.	Create a base class Animal with a method sound(). Create subclasses Dog, Cat, Cow, and Lion. Override sound() in each class to display the appropriate sound.

class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes a generic sound.")


class Dog(Animal):
    def sound(self):
        print(f"Dog [{self.name}]: Bark! Bark! (Woof!)")


class Cat(Animal):
    def sound(self):
        print(f"Cat [{self.name}]: Meow! Purr~")


class Cow(Animal):
    def sound(self):
        print(f"Cow [{self.name}]: Moo! Moo!")


class Lion(Animal):
    def sound(self):
        print(f"Lion [{self.name}]: Roar!!")


animals = [
    Dog("Bruno"),
    Cat("Luna"),
    Cow("Kamadhenu"),
    Lion("Simba")
]

print("Animal Sounds")
for a in animals:
    a.sound()
