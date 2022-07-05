#!/usr/bin/python3
"""
Modules for reading file [with]
"""


def read_file(filename=""):
    """
    Function returning the contentsof a file
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end="")
