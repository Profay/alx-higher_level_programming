#!/usr/bin/python3
"""
Define Function Pascal's triangle
"""


def pascal_triangle(n):
    """ returns a list of lists of integers
    representing the Pascal's triangle of n"""
    if n <= 0:
        return []
