#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    for a in range(0, len(my_list)):
        if idx != a:
            return my_list
        else:
            del my_list[idx]
            return my_list
