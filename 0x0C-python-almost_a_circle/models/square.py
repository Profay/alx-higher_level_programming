#!/usr/bin/python3
""" Now Square subclass
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ the init method for class square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''Returns string info about this square.'''
        return "[Square] ({}) {}/{} - {}" \
            .format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """ getter method for size
        """
        return self.width

    @size.setter
    def size(self, value):
        """ setter method for size
        """
        self.width = value
        self.height = value

    def args_update(self, id=None, size=None, x=None, y=None):
        """ Updating the class Rectangle by assigning arguments
        to each attributes """
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """ Updates the both keyword and non-keyword arguments
        """
        if args:
            self.args_update(*args)
        else:
            self.args_update(**kwargs)

    def to_dictionary(self):
        """ Returns the dictionary representation of a class square
        """
        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}
