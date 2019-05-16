from prac_08.unreliable_car import UnreliableCar

car1 = UnreliableCar("Reliable", 100, 80)
car2 = UnreliableCar("Unreliable", 100, 10)

for i in range(1, 50):
    print("Reliable car drove {}km".format(i))
    print("Unreliable car drove {}km".format(i))
