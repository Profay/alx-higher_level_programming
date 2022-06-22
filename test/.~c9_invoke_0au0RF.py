#!/usr/bin/python3

class Square:

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        
        self.__position[]

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

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size != 0:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end="")
                print("")
        else:
            print(" ")

    @property
    def position(self):
        return self.__position()

    @position.setter
    def position(self, value):
        for i in self.__position:
            if type(self.__position[i]) is not int:
                raise TypeError("position must be a tuple of 2 positive integers")
            elif self.position[i] < 0:
                 TypeError("position must be a tuple of 2 positive integers")
            else:
                self.__position[i] = value[i]
