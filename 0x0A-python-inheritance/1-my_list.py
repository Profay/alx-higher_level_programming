#!/usr/bin/python3
""" class inheritance
"""


class MyList(list):
    """ a subclass of integer lists
    """

    def print_sorted(self):
        """ function that prints a sorted list of integers
        """
        print(sorted(self))
