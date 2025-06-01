num1 = int(input("Enter the first number:"))
num2 =int (input("Enter the second number:"))
operation_type = input("Choose the operation (+, -, *, /):")
match operation_type:
    case "+":
          print(num1 + num2)
    case "-":
          print(num1 - num2)      
    case "*":
          print(num1 * num2)
    case "/":
          if num1 == 0 or num2 == 0:
              print("Cannot divide by zero.")        
          else:
            print(num1 / num2)
    case _:
        print("Invalid operation.")                                   
    