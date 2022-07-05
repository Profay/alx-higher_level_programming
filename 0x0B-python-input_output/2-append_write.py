#!/usr/bin/python3
"""
Modules for appending file [with]
"""


def append_write(filename="", text=""):
    """
    Function for appending new contents to a file
    Returning the lenght of the text
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        return file.write(text)
