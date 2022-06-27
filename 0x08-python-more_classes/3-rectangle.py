#!/usr/bin/python3
"""
Module Rectangle
"""


class Rectangle:
    """
    Declaring a class for rectangle
    Rectangle will have its width and height
    Cases of Area might be included later on.
    """
    def __init__(self, width=0, height=0):
        """
        Declaring the init method for rectangle of width and height
        """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """
        Returns the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the value of the width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Return the value of the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets the value of height
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        return the product of the width and height of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Return the addition of all sides of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return ((self.__width + self.__height) * 2 )
            
    def __str__(self):
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                if self.__width != 0 or self.__height != 0:
                    print("#", end="")
                else:
                    print("")
            print("")
        return "a"