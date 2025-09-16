#calculator that propmts the user to enter two numbers and select an operation.

#prompt for user input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

#calculation using match case
match operation:
    case '+':
        print(f"The result is {num1 + num2}")
    case '-':
        print(f"The result is {num1 - num2}")
    case '*':
        print(f"The result is {num1 * num2}")
    case '/':
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            print(f"The result is {num1 / num2}")
