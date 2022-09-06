#!/usr/bin/python3
""" checking an instance of a class
"""


def is_same_class(obj, a_class):
    """ function that returns True if an object is exactly an
    instance of the specified class; otherwise False.
    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    """
    if type(obj) == a_class:
        return True
    return False
