print("=" * 30)
print("          CALCULATOR")
print("=" * 30)
val_1 = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
val_2 = float(input("Enter second number: "))

if op == "+":
    output = val_1 + val_2
elif op == "-":
    output = val_1 - val_2
elif op == "*":
    output = val_1 * val_2
elif op == "/":
    if val_two != 0:
        output = val_1 / val_2
    else:
        output = "Cannot divide by zero"
else:
    output = "Invalid operator"

print("-" * 30)
print("Result:", output)
print("=" * 30)
