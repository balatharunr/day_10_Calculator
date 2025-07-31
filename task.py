logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
def add(n1, n2):
    return n1 + n2
def subtract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    if n2 == 0:
        return "Error: Division by zero"
    return n1 / n2
operations = {"+": add, "-": subtract, "*": multiply, "/": divide}
print(logo)
def calculator():
    num1 = float(input("Enter Num1: "))
    should_continue = True
    while should_continue:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("Enter Num2: "))
        calculation_function = operations[operation_symbol]
        result = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {result}")
        choice = input("Type 'y' to continue with result or 'n' to start new calculation: ").lower()
        if choice == "y":
            num1 = result
        else:
            should_continue = False
            calculator()
calculator()
