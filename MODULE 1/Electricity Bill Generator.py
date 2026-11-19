customer_name = input("Enter Consumer Name: ")
customer_id = input("Enter Consumer ID: ")
prev_reading = float(input("Enter Previous Reading: "))
curr_reading = float(input("Enter Current Reading: "))
unit_rate = float(input("Enter Cost per Unit: "))

consumed_units = curr_reading - prev_reading
power_cost = consumed_units * unit_rate
tax_amount = power_cost * 0.05
meter_fee = 100
final_bill = power_cost + tax_amount + meter_fee

print("\nElectricity Bill")
print("Consumer Name =", customer_name)
print("Consumer ID =", customer_id)
print("Units Consumed =", consumed_units)
print("Energy Charge =", power_cost)
print("Electricity Duty =", tax_amount)
print("Fixed Meter Charge =", meter_fee)
print("Net Bill Amount =", final_bill)
