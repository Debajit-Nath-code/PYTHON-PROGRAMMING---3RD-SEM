import csv
import matplotlib.pyplot as plt

revenue_data = {
    "Laptop": 65000,
    "Mobile": 42000,
    "Tablet": 25000,
    "Headphones": 15000
}

with open("sales.csv", "w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Product", "Sales"])
    for item_name, rev in revenue_data.items():
        csv_writer.writerow([item_name, rev])

print("Retail Sales Report")
for item_name, rev in revenue_data.items():
    print(item_name, ":", rev)

overall_rev = sum(revenue_data.values())
print("Total Sales:", overall_rev)

plt.bar(revenue_data.keys(), revenue_data.values())
plt.title("Retail Sales Dashboard")
plt.xlabel("Products")
plt.ylabel("Sales Amount")
plt.show()
