#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        s = " "
        print("{}".format(s.join(map(str, i))))
