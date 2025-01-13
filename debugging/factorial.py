#!/usr/bin/python3
import sys

def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if len(sys.argv) < 2:
    print("Usage: python3 script.py <number>")
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("Error: The input must be an integer.")
    sys.exit(1)

if n < 0:
    print("Error: The input must be a non-negative integer.")
    sys.exit(1)

f = factorial(n)
print(f)

