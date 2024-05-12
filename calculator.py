# Implement a class representing a basic calculator that can perform addition, subtraction,
# multiplication, and division.
# The class should have the following methods:
# - add(a, b): returns the sum of a and b
# - subtract(a, b): returns the difference of a and b,
#   it should always return a positive number whether a or b is greater
# - multiply(a, b): returns the product of a and b
# - divide(a, b): returns the division of a and b
# Example: calculator.py add 1 2, Output: 3
# Example: calculator.py subtract 2 1, Output: 1
# Example: calculator.py multiply 2 3, Output: 6
# Example: calculator.py divide 4 2, Output: 2
# Example: calculator.py divide 4 0, Output: Division by zero is not allowed
# You can use the argparse module to parse the command-line arguments.
# The first argument is the operation to perform, followed by two numbers.
# The operation can be add, subtract, multiply, or divide, else print "Invalid operation"

import argparse


class Calculator:
    def __init__(self):
        pass

    def add(self, a, b):
        return f'Result = {a + b}'

    def subtract(self, a, b):
        return f'Result = {abs(a - b)}'

    def multiply(self, a, b):
        return f'Result = {a * b}'

    def divide(self, a, b):
        if b == 0:
            return "Division by zero is not allowed"
        # return f'Result = {a // b}'     # return only integer part of the division
        # return f'Result = {a / b}'     # return float value of the division
        return f'Result = {a / b:.2f}'  # return float value of the division with 2 decimal places


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('operation', type=str, help='Operation to perform')
    parser.add_argument('a', type=int, help='First number')
    parser.add_argument('b', type=int, help='Second number')
    args = parser.parse_args()
    calculator = Calculator()
    if args.operation == 'add':
        print(calculator.add(args.a, args.b))
    elif args.operation == 'subtract':
        print(calculator.subtract(args.a, args.b))
    elif args.operation == 'multiply':
        print(calculator.multiply(args.a, args.b))
    elif args.operation == 'divide':
        print(calculator.divide(args.a, args.b))
    else:
        print("Invalid operation")