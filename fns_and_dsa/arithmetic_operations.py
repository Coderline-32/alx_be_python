def perform_operation(num1, num2, operation):
    try:
        # Ensure inputs are the correct types
        if not isinstance(operation, str):
            return "Error: Operation must be a string"

        # Try converting to float (if not already)
        num1 = float(num1)
        num2 = float(num2)

        if operation == "add":
            return num1 + num2
        elif operation == "subtract":
            return num1 - num2
        elif operation == "multiply":
            return num1 * num2
        elif operation == "divide":
            if num2 == 0:
                return "Error: Division by zero"
            return num1 / num2
        else:
            return "Error: Invalid operation"
    
    except (ValueError, TypeError):
        return "Error: Invalid input"
