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
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Declaring the init method for rectangle of width and height
        """
        self.__height = height
        self.__width = width
        type(self).number_of_instances += 1

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
            return ((self.__width + self.__height) * 2)

    def __str__(self):
        print_string = ""
        if self.__width == 0 or self.__height == 0:
            return print_string
        else:
            for i in range(0, self.__height):
                for j in range(0, self.__width):
                    print_string += str(self.print_symbol)
                if i < self.__height - 1:
                    print_string += "\n"
            return print_string

    def __repr__(self):
        """
        Instance Method : repr
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """
        Instance Method : delete & message
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Instance Method : bigger_or_equal
        """
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if rect_1.area() > rect_2.area():
                return rect_1
            elif rect_1.area() == rect_2.area():
                return rect_1
            else:
                return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Instance Method : square
        """
        return Rectangle(size, size)
