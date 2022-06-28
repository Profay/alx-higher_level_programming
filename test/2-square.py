#!/usr/bin/python3

class Node:
    """
    declaring class attribute
    class Node has data instance
    Next and Prev as attributes
    """
    data = 0
    next_node = None
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node
        
        
    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value
    @property
    def next_node(self):
        return self.__next_node
    
    @next_node.setter
    def next_node(self, value):
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value
    
class SinglyLinkedList:
    def __init__(self):
        self.__head = None
    def sorted_insert(self, value):
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
