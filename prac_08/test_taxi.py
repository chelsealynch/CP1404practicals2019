from prac_08.taxi import Taxi

taxi = Taxi("Prius 1", 100, Taxi.price_per_km)
taxi.drive(40)
print(taxi)
taxi.start_fare()
taxi.drive(100)
print(taxi)