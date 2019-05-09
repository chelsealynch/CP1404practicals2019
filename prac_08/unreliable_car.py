from prac_08.car import Car
import random


class UnreliableCar(Car):
    reliability = random.uniform(0, 100)

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.name = name
        self.fuel = fuel
        self.reliability = reliability

    def drive(self, distance):
        distance_driven = super().drive(distance)
        self.distance = distance_driven
