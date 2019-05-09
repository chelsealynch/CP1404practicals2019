from prac_08.car import Car
import random


class UnreliableCar(Car):
    reliability = random.random(0, 100)
    distance = random.random

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.name = name
        self.fuel = fuel
        self.reliability = reliability

    def drive(self, distance):
        self.distance = distance
        if distance
