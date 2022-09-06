#!/usr/bin/python3
""" An empty class
"""


class BaseGeometry:
    """ defines an BaseGeometry class
    """
    def area(self):
        """ area of the Geometry
        """
        raise Exception("area() is not implemented")
