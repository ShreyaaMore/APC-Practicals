# 17.	Create a base class Animal with common attributes and methods. Derive Dog, Cat, and Cow classes and implement their specific sounds and behaviors.

class Animal:
    def __init__(self, name, species, diet):
        self.name = name
        self.species = species
        self.diet = diet

    def eat(self):
        print(f"{self.name} ({self.species}) is eating {self.diet} food.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog", "omnivore")
        self.breed = breed

    def sound(self):
        print(f"{self.name} says: Woof! Woof!")

    def fetch(self):
        print(f"{self.name} the {self.breed} is fetching the ball!")


class Cat(Animal):
    def __init__(self, name, is_indoor=True):
        super().__init__(name, "Cat", "carnivore")
        self.is_indoor = is_indoor

    def sound(self):
        print(f"{self.name} says: Meow~ Meow~")

    def scratch(self):
        print(f"{self.name} is scratching the scratching post.")


class Cow(Animal):
    def __init__(self, name, milk_yield_liters):
        super().__init__(name, "Cow", "herbivore")
        self.milk_yield_liters = milk_yield_liters

    def sound(self):
        print(f"{self.name} says: Moo! Moo!")

    def graze(self):
        print(f"{self.name} is grazing in the meadow (Milk yield: {self.milk_yield_liters} L/day).")


dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers")
cow = Cow("Gauri", 12.5)

animals = [dog, cat, cow]
print("Animals and Their Behaviors")
for a in animals:
    a.eat()
    a.sound()
    if isinstance(a, Dog):
        a.fetch()
    elif isinstance(a, Cat):
        a.scratch()
    elif isinstance(a, Cow):
        a.graze()
    print("-" * 35)
