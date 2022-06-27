#!/usr/bin/python3

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
        self.__width = width
        self.__height = height
        
    @property
    def width(self):
        return self.__width
        
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
    
    @property
    def height(self):
        return self.__height
        
    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
