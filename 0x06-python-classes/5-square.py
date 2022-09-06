#!/usr/bin/python3
""" Module Sqaure """


class Square:
    """ Definition of a Class Square
        Attributes :
                  size (int): Size of square
    """
    def __init__(self, size=0):
        """initializes the square
        Args:
            size (int): size of a side of the square
        """
        self.__size = size

    def area(self):
        """
        set  square area
        Return:
            the current square area (int)
        """
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for x in range(0, self.__size):
                for y in range(0, self.__size):
                    print("#", end="")
                print()
