"""Exercise 1"""

# names = ["Jack", "Jill", "Harry"]
# dates_of_birth = [(12, 4, 1999), (1, 1, 2000), (27, 3, 1982)]

NAMES_AND_DOB = {"Jack": "12/4/1999", "Jill": "1/1/2000", "Harry": "27/3/1982"}

"""Exercise 2"""

#  later

"""Exercise 3"""

tariffs = {"TARIFF_11": 0.244618, "TARIFF_31": 0.136928}

print("\nElectricity bill estimator 2.0")
tariff = int(input("Which tariff? 11 or 31: "))
daily_use = float(input("Enter daily use: "))
number_billing_days = int(input("Enter number of billing days: "))
if tariff == 11:
    estimated_bill = tariffs["TARIFF_11"] * daily_use * number_billing_days
elif tariff == 31:
    estimated_bill = tariffs["TARIFF_31"] * daily_use * number_billing_days
print("Estimated bill: ${:.2f}".format(estimated_bill))
