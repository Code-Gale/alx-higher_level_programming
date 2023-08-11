#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

if len(sys.argv) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit (1)

    a = int(arg[1])
    operator = arg[2]
    b = int(arg[3])

    if operator == '+':
        result = add
    elif operator == '-':
        result = sub
    elif operator == '*':
        result = mul
    elif operator == '/':
        result = div
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit (1)
