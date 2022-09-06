#!/usr/bin/python3
""" a subclass of in-built class int
"""


class MyInt(int):
    """ a subclass of int that inverts int operators
    == and !=
    """

    def __eq__(self, value):
        """Override == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior."""
        return self.real == value
