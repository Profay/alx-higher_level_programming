#!/usr/bin/python3
"""
Modules for adding two integer together
Two parameters are passed and the sum is returned if value.
If nothing is passed for b, b assumed a default value of 89.
"""


def add_integer(a, b=98):
    """
    Taking two integers and returning the sum
    b is 89 by default
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
