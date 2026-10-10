#2. Duck typing -
#                Another way to achieve polymorphism other than inheritence
#                object must have minimum necessary attributes/methods

class Animals:
    can_breathe = True

class Tiger(Animals):
    def speak(self):
        print("Roar")

class Cat(Animals):
    def speak(self):
        print("Meow")

class Bike:
    can_breathe = False
    def speak(self):
        print("Vroom")

animals = [Tiger(),Cat(),Bike()]

for animal in animals:
    animal.speak()
    print(animal.can_breathe) 