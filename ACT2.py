# Base class
class Vehicle:
    def move(self):
        return "Vehicle is moving..."

# Derived classes
class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing 🚢"

# Polymorphism in action
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    print(v.move())
