#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list == []:
        a = None
        return a
    else:
        my_list.sort()
        return my_list.pop()
