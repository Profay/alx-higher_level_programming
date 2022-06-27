#!/usr/bin/python3
"""
    Module Rectangle
"""


class Rectangle:
    """
        Definition of a Class Rectangle
            Initializing number_of_instances to 0
            Initializing print_symbol to #
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        The instance method called when a new object is created
        Args:
            width : a private attribute
            height : a private attribute
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        width getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        width setter
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        height getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        height setter
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Public Instance : Area
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Public Instance : Perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """
        Instance Method : str
        """
        print_string = ""
        if self.__width == 0 or self.__height == 0:
            return print_string
        else:
            for x in range(0, self.__height):
                for y in range(0, self.__width):
                    print_string += str(self.print_symbol)
                if x < self.__height - 1:
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
        Rectangle.number_of_instances -= 1
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
