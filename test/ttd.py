#!/usr/bin/python3

def matrix(rows, column):
    matrix = []
    for row in range(rows):
        matrix += [[0] * column]
    return matrix
        

print(matrix(4, 5))
m = matrix(4,5)
m[1][1] = 8
m[2][4] = 4
print(m)