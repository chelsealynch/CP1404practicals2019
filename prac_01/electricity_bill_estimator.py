# print("Electricity bill estimator")
# cents_per_kWh = int(input("Enter cents per kWh: "))
# daily_use = float(input("Enter daily use: "))
# number_billing_days = int(input("Enter number of billing days: "))
# estimated_bill = (cents_per_kWh / 100) * daily_use * number_billing_days
# print("Estimated bill: ${}".format(estimated_bill))

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("\nElectricity bill estimator 2.0")
tariff = int(input("Which tariff? 11 or 31: "))
daily_use = float(input("Enter daily use: "))
number_billing_days = int(input("Enter number of billing days: "))
if tariff == 11:
    estimated_bill = TARIFF_11 * daily_use * number_billing_days
elif tariff == 31:
    estimated_bill = TARIFF_31 * daily_use * number_billing_days
print("Estimated bill: ${}".format(estimated_bill))