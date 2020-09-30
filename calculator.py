print("Simple Calculator")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")
print("5.Perentage")
print("5.Quit")
while True:
    option = int(input("Enter the number:  "))
    if option == 5:
        break
    elif option == 1:
        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))
        print(number1 + number2)
    elif option == 2:
        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))
        print(number1 - number2)
    elif option == 3:
        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))
        print(number1 * number2)
    elif option == 4:
        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))
        print(number1 / number2)
    else : 
        print("Invalid Input")
print("EXIT")
