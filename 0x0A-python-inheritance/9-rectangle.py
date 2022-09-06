#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ a rectangle class which is a subclass of class BaseGeometry
    """
    def __init__(self, width, height):
        """ init method for rectangle class
        """
        self.__width = width
        self.__height = height

        super().integer_validator("width", width)
        super().integer_validator("height", height)

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        """ print """
        return ("[Rectangle] " + str(self.__width) + "/" + str(self.__height))
