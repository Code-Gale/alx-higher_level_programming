#!/usr/bin/python3
"""
This function adds 2 integers and returns
the sum
"""


def add_integer(a, b=98):
    """
    Calculates the sum of two ints
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
