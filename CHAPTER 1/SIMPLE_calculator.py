print("Choose an operation:")
print(" + : Addition")
print(" - : Subtraction")
print(" * : Multiplication")
print(" / : Division")

try:
    num1 = float(input("\nEnter the first number: "))
    operator = input("Enter an operator +, -, *, / : ")
    num2 = float(input("Enter the second number: "))
    
    if operator == '+':
        result = num1 + num2
        print(f"\nResult: {num1} + {num2} = {result}")
        
    elif operator == '-':
        result = num1 - num2
        print(f"\nResult: {num1} - {num2} = {result}")
        
    elif operator == '*':
        result = num1 * num2
        print(f"\nResult: {num1} * {num2} = {result}")
        
    elif operator == '/':
        if num2 == 0:
            print("\nError: Cannot divide by zero!")
        else:
            result = num1 / num2
            print(f"\nResult: {num1} / {num2} = {result}")        
    else:
        print("\nError: Invalid operator selected.")

except ValueError:
    print("\nError: Please enter valid numbers.")
