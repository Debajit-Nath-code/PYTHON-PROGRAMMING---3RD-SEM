import csv

with open("payroll.csv", "w", newline="") as out_csv:
    csv_out = csv.writer(out_csv)
    csv_out.writerow(["Name", "Basic Salary", "Bonus", "Total"])
    staff_count = int(input("Enter number of employees: "))
    for _ in range(staff_count):
        emp_name = input("Enter employee name: ")
        base_pay = float(input("Enter basic salary: "))
        extra_pay = float(input("Enter bonus: "))
        gross_pay = base_pay + extra_pay
        csv_out.writerow([emp_name, base_pay, extra_pay, gross_pay])

with open("payroll.csv", "r") as in_csv:
    csv_in = csv.reader(in_csv)
    print("\nPayroll Details:")
    for record in csv_in:
        print(record)
