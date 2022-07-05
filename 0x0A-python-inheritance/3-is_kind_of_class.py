#!/usr/bin/python3
""" Checks if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class
"""


def is_kind_of_class(obj, a_class):
    """ function that returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class, Otherwise, False
    """
    if isinstance(obj, a_class):
        return True
    return False
