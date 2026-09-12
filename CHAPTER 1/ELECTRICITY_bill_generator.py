name = input("Enter Consumer Name: ")
id = input("Enter Consumer ID: ")
previous = float(input("Enter Previous Reading: "))
current = float(input("Enter Current Reading: "))
cost = float(input("Enter Cost per Unit: "))

units = current - previous
energy = units * cost
duty = energy * 0.05
fixed = 100
total = energy + duty + fixed

print("Electricity Bill")
print("Consumer Name: ", name)
print("Consumer ID: ", id)
print("Units Consumed:", units)
print("Energy Charge:", energy)
print("Electricity Duty: ", duty)
print("Fixed Charge: ", fixed)
print("Net Bill: ", total)