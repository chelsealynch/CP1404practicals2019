from prac_08.unreliable_car import UnreliableCar

car1 = UnreliableCar("Reliable", 100, 80)
car2 = UnreliableCar("Unreliable", 100, 10)

for i in range(1, 100):
    distance = car1.drive(1)
    print("Reliable car drove {}km".format(distance), end=" ")
    distance = car2.drive(1)
    print("Unreliable car drove {}km".format(distance))

print(car1)
print(car2)