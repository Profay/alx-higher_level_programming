#!/usr/bin/python3

class Node:
    """
    declaring class attribute
    class Node has data instance
    Next and Prev as attributes
    """
    data = 0
    next_node = N
    def __init__(self, data, next_node=None):
    """
    declaring class attribute
    class Node has data instance
    Next and Prev as attributes
        """
        self.__data = data
        self.__next_node = next_node
        
        
    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else
            self.__data = value
    @property
    def next_node(self):
        return self.__next_node
    
    @next_node.setter
    def next_node(self, value):
        