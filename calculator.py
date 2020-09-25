while True:
    option = input("Enter the string 'add' or 'subtract' or 'multiply' or 'divide' or 'quit' :  ")
    if option == 'quit':
        break
    elif option == 'add':
        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))
        print(number1 + number2)
    elif option == 'subtract':
        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))
        print(number1 - number2)
    elif option == 'multiply':
        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))
        print(number1 * number2)
    elif option == 'divide':
        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))
        print(number1 / number2)
    else : 
        print("Invalid Input")
print("EXIT")