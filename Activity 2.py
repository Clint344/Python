# Base class
class Vehicle:
    def move(self):
        print("The vehicle moves.")

# Subclasses overriding the move method
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing ⛵")

# List of different vehicles
vehicles = [Car(), Plane(), Boat()]

# Loop to demonstrate polymorphism
for vehicle in vehicles:
    vehicle.move()
