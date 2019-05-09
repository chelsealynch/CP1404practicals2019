from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):

    def __init__(self, name, fuel, fanciness):
        self.name = name
        self.fuel = fuel
        self.fanciness = fanciness