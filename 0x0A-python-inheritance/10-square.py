#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ square class that inherits rectangle class
    """
    def __init__(self, size):
        self.__size = size

        super().integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        return self.__size ** 2
