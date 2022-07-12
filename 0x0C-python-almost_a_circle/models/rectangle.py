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

    def area(self):
        """ Function returning the area of the rectangle
        """
        return self.__height * self.__width

    def display(self):
        """ This method prints the rectangle instance
        with character '#'
        """
        rectangle = '\n' * self.y + \
            (' ' * self.x + '#' * self.width + '\n') * self.height
        print(rectangle, end='')

    def __str__(self):
        """ overriding str  method
        """
        return "[Rectangle] ({}) {}/{} - {}/{}" \
            .format(self.id, self.__x, self.__y, self.__width, self.__height)

    def args_update(self, id=None, width=None, height=None, x=None, y=None):
        """ Updating the class Rectangle by assigning arguments
        to each attributes """
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """ This method updates instance attributes via
        no-keyword & keyword arguments
        """
        if args:
            self.args_update(*args)
        else:
            self.args_update(**kwargs)

    def to_dictionary(self):
        """ Returns the dictionary representation of class
        square """
        return {"id": self.id, "width": self.__width,
                "height": self.__height, "x": self.__x, "y": self.__y}
