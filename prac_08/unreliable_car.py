from prac_08.car import Car
from random import randint


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        self.name = name
        self.fuel = fuel
        self.reliability = reliability

    def drive(self, distance):
        car_reliability = randint(1, 100)
        if car_reliability >= self.reliability:
            distance = 0
        distance_driven = self.drive(distance)
        return distance_driven
