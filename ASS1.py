# Base class
class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self._power = power     # Encapsulated attribute
        self.origin = origin

    def show_identity(self):
        return f"My name is {self.name} and I fight for justice!"

    def use_power(self):
        return f"{self.name} uses {self._power}!"

    # Encapsulation: getter and setter for power
    def get_power(self):
        return self._power

    def set_power(self, new_power):
        self._power = new_power

# Derived class
class FlyingHero(Superhero):
    def __init__(self, name, power, origin, flight_speed):
        super().__init__(name, power, origin)
        self.flight_speed = flight_speed

    def use_power(self):
        return f"{self.name} soars at {self.flight_speed} km/h using {self._power}!"

# Test objects
hero1 = Superhero("ShadowStrike", "Invisibility", "Moon City")
hero2 = FlyingHero("SkyBlazer", "Wind Gust", "Cloud Realm", 800)

# Test methods
print(hero1.show_identity())
print(hero1.use_power())

print(hero2.show_identity())
print(hero2.use_power())
