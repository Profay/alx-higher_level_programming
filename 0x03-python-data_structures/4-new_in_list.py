#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    new_list = my_list[:]
    a = len(new_list) - 1
    if idx >= 0 and idx <= a:
        new_list[idx] = element
        return new_list
    else:
        return my_list
