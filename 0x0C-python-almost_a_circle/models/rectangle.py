#!/usr/bin/python3
"""Modules for class base
It takes a private instance object
"""
from models.base import Base


class Rectangle(Base):
    """Declaring a class that inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """The rectangle class constructor
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Function for getting the width of the rectangle
        """
        return self.__width
    @width.setter
    def width(self, value):
        """ Function setting the width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value
    
    @property
    def height(self):
        """ Function for getting height of the rectangle
        """
        return self.__height
    @height.setter
    def height(self, value):
        """ Function setting the height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value
    
    @property
    def x(self):
        """ Function for getting x of the rectangle
        """
        return self.__x
    @x.setter
    def x(self, value):
        """ Function setting the x
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value
    @property
    def y(self):
        """ Function for getting y of the rectangle
        """
        return self.__y
    @y.setter
    def y(self, value):
        """ Function setting the y
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value
    