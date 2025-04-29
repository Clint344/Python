# Base class using encapsulation
class Superhero:
    def __init__(self, name, power, health):
        self.name = name
        self._power = power        # Protected attribute
        self.__health = health     # Private attribute

    def display_info(self):
        print(f"Name: {self.name}, Power: {self._power}")

    def get_health(self):         # Getter for private attribute
        return self.__health

    def take_damage(self, damage):
        self.__health -= damage
        print(f"{self.name} took {damage} damage! Health is now {self.__health}")

# Subclass with inheritance and method overriding (polymorphism)
class FlyingHero(Superhero):
    def __init__(self, name, power, health, flight_speed):
        super().__init__(name, power, health)
        self.flight_speed = flight_speed

    def display_info(self):  # Overriding method
        super().display_info()
        print(f"Flight Speed: {self.flight_speed} km/h")

# Create an instance of the subclass
hero1 = FlyingHero("SkyBlaze", "Fire Wings", 100, 500)

# Use the methods
hero1.display_info()
hero1.take_damage(20)
print(f"Current Health: {hero1.get_health()}")
