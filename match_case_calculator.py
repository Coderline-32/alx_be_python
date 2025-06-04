num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Choose the operation (+, -, *, /): ")

match operator:
    case "+":
        output = num1 + num2
        print(f"The result is {output}")
    case "-":
        output = num1 - num2
        print(f"The result is {output}")
    case "*":
        output = num1 * num2
        print(f"The result is {output}")
    case "/":
        if num2 != 0:
            output = num1/num2
        else:
            print("Cannot divide by zero!")
            
    case _:
        print("Invalid operator.")
       
