#!/usr/bin/python3
import sys

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Check if a valid argument was passed
if len(sys.argv) != 2:
    print("Usage: python3 factorial.py <number>")
    sys.exit(1)

try:
    number = int(sys.argv[1])  # Convert the argument to an integer
except ValueError:
    print("Error: Please provide a valid integer.")
    sys.exit(1)

# Compute and print the factorial
try:
    result = factorial(number)
    print(f"The factorial of {number} is {result}")
except ValueError as e:
    print(e)
    sys.exit(1)

