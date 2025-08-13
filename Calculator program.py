try:
    # number input
    num1_str = input("Enter the first number: ")
    num1 = float(num1_str)
    num2_str = input("Enter the second number: ")
    num2 = float(num2_str)
    
    # operation
    operation = input("Enter an operation (+, -, *, /): ")
    
    # calculation operation
    if operation == "+":
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operation == "-":
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operation == "*":
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operation == "/":
        if num2 == 0:
            print("Error: Cannot divide by zero!")
        else:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
    else:
        print("Error! Invalid operation.")
        
except ValueError:
    print("Error! Invalid numbers.")