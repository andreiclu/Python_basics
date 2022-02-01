class Vehicle():
    def __init__(self, max_speed, milege, name, capacity):
        self.max_speed = max_speed
        self.milege = milege
        self.name = name
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

    def seating_capacity(self):
        return f"The seating capacity of a {self.name} is {self.capacity} passengers"

class Bus(Vehicle):
    def fare(self):
        return super().fare() * 1.1














