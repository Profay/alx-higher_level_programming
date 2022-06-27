#!/usr/bin/python3
"""
Modules for adding two integer together
"""


def add_integer(a, b=98):
    """
    taking two integers and returning the sum
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
