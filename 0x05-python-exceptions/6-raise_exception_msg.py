#!/usr/bin/python3


def raise_exception_msg(message=""):
    try:
        raise TypeError
    except TypeError:
        print("{}".format(message))
