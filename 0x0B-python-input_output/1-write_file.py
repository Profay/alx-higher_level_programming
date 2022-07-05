#!/usr/bin/python3
"""
Modules for reading file [with]
"""


def read_file(filename="", letters=""):
    """
    Function for writing new contents to a file
    Returning the lenght of the text
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        return file.write(letters)
