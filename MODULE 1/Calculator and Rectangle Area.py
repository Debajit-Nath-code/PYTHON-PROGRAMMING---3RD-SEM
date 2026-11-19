print("=" * 30)
print("        CALCULATOR")
print("=" * 30)

val_one = float(input("Enter first number: "))
op_symbol = input("Enter operator (+, -, *, /): ")
val_two = float(input("Enter second number: "))

if op_symbol == "+":
    output = val_one + val_two
elif op_symbol == "-":
    output = val_one - val_two
elif op_symbol == "*":
    output = val_one * val_two
elif op_symbol == "/":
    if val_two != 0:
        output = val_one / val_two
    else:
        output = "Cannot divide by zero"
else:
    output = "Invalid operator"

print("-" * 30)
print("Result:", output)
print("=" * 30)
