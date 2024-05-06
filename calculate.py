def calculator(num1, operation_symbol, num2, continue_operation, new_operation):
    def add(n1, n2):
        return n1 + n2

    def subtract(n1, n2):
        return n1 - n2

    def multiply(n1, n2):
        return n1 * n2

    def divide(n1, n2):
        return n1 / n2

    operations = {
    "+": "add",
    "-": "subtract",
    "*": "multiply",
    "/": "divide",
    }

    def calculation():
        if operation_symbol == "+":
            return add(num1, num2)
        elif operation_symbol == "-":
            return subtract(num1, num2)
        elif operation_symbol == "*":
            return multiply(num1, num2)
        elif operation_symbol == "/":
            return divide(num1, num2)
        else:
            return "You entered an invalid symbol."

    num1 = float(input("Enter the first number: "))

    should_continue = True
    while should_continue: 
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("Enter the next number: "))
        answer = calculation()
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        continue_operation = input(f"Do you wish to perform another operation with {answer}? Type 'yes' or 'no': ")
        if continue_operation == "yes":
            num1 = answer
        elif continue_operation == "no":
            new_operation = input("Do you wish to start a new operation? Type 'yes' or 'no': ")
            if new_operation == "yes":
                num1 = float(input("Enter the first number: "))
            else:
                should_continue = False
                print("Okay. Bye")
            
        
