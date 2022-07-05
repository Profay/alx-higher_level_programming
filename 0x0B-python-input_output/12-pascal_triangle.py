#!/usr/bin/python3
"""
Define Function Pascal's triangle
"""


def pascal_triangle(n):
    """ returns a list of lists of integers
    representing the Pascal's triangle of n"""
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    triangle = []
    for i in range(n):
        row = [0] * (i + 1)
        triangle.append(row)
    triangle[0][0] = 1
    for row in range(n - 1):
        for col in range(len(triangle[row])):
            triangle[row + 1][col] += triangle[row][col]
            triangle[row + 1][col + 1] += triangle[row][col]
    return triangle
