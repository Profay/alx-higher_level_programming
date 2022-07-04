#!/usr/bin/python3
"""
Define the Mylist class
"""


class MyList(list):
    """ Subclass of list """
    def print_sorted(self):
        """ prints list sorted """
        print(sorted(self))
