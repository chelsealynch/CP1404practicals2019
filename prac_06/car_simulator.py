from prac_06.car import Car

def main():
    print("Let's drive!")
    car_name = input("Enter your car name: ")
    car = Car(car_name, 100)
    print(car)
    print("Menu:")
    print("d) drive")
    print("r) refuel")
    print("q) quit")
    user_choice = input("Enter your choice: ").lower()
    while user_choice != "q":
        if user_choice == "d":
            distance_to_drive = int(input("How many km do you wish to drive? "))
            while distance_to_drive < 0:
                print("Distance must be >= 0")
                distance_to_drive = int(input("How many km do you wish to drive? "))
            distance_driven = car.drive(distance_to_drive)
            print("The car drove {}km".format(distance_driven))
            if car.fuel == 0:
                print(" and ran out of fuel")
            print(".")
        elif user_choice == "r":
            fuel_to_add = int(input("How many units of fuel do you want to add? "))
            while fuel_to_add < 0:
                print("Fuel amount must be >= 0")
                fuel_to_add = int(input("How many units of fuel do you want to add?"))
            car.add_fuel(fuel_to_add)
            print("Added {} units of fuel.".format(fuel_to_add))
        else:
            print("Invalid choice")
        print(car)
        print("Menu:")
        print("d) drive")
        print("r) refuel")
        print("q) quit")
        user_choice = input("Enter your choice: ").lower()
    print("\nGoodbye {}'s driver.".format(car.name))


main()