# Prompt the user for inputs
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation_type = input("Choose the operation (+, -, *, /): ")

# Perform the calculation using match-case
match operation_type:
    case "+":
        result = num1 + num2
        print(f"The result is {result}.")
    case "-":
        result = num1 - num2
        print(f"The result is {result}.")
    case "*":
        result = num1 * num2
        print(f"The result is {result}.")
    case "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result is {result}.")
    case _:
        print("Invalid operation. Please choose one of +, -, *, /.")
