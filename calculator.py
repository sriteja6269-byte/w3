class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Error: Cannot divide by zero!"


# Create calculator object
calc = Calculator()

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("\nChoose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print("Result:", calc.add(num1, num2))

    elif choice == "2":
        print("Result:", calc.subtract(num1, num2))

    elif choice == "3":
        print("Result:", calc.multiply(num1, num2))

    elif choice == "4":
        print("Result:", calc.divide(num1, num2))

    else:
        print("Invalid choice!")

except ValueError:
    print("Error: Please enter numbers only!")