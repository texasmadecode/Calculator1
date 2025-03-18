import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def square(a):
    return a ** 2

def power(a, b):
    return math.pow(a, b)

def square_root(a):
    if a < 0:
        return "Error: Cannot compute square root of a negative number"
    return math.sqrt(a)

def is_even(a):
    return "Even" if a % 2 == 0 else "Odd"

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def log(base, x):
    if base <= 0 or base == 1:
        return "Error: Log base must be greater than 0 and not equal to 1"
    if x <= 0:
        return "Error: Logarithm argument must be positive"
    return math.log(x, base)

def main():
    operations = {
        1: ("Add", add),
        2: ("Subtract", subtract),
        3: ("Multiply", multiply),
        4: ("Divide", divide),
        5: ("Square", square),
        6: ("Power", power),
        7: ("Square Root", square_root),
        8: ("Odd/Even", is_even),
        9: ("Check if Prime", is_prime),
        10: ("Log", log)
    }
    
    while True:
        print("\nSimple Calculator")
        for key, (name, _) in operations.items():
            print(f"{key}. {name}")
        print("11. Quit")

        try:
            option = int(input("Enter a number to execute operation: "))
            if option == 11:
                break

            if option in operations:
                operation_name, operation_func = operations[option]
                
                if option in {1, 2, 3, 4, 6}:  # Two-operand operations
                    number1 = float(input("Enter first number: "))
                    number2 = float(input("Enter second number: "))
                    result = operation_func(number1, number2)
                elif option in {5, 7, 8}:  # Single-operand operations
                    number = float(input("Enter a number: "))
                    result = operation_func(number)
                elif option == 9:
                    number = int(input("Enter a number to check if it is prime: "))
                    result = "Prime" if operation_func(number) else "Not Prime"
                elif option == 10:
                    base = float(input("Enter logarithm base: "))
                    x = float(input("Enter number to calculate: "))
                    result = operation_func(base, x)
                
                print(f"Result: {result}")
            else:
                print("Invalid Input")
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")
        except Exception as e:
            print(f"Error: {e}")
    
    print("EXIT")

if __name__ == "__main__":
    main()
