#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    for i in range(0, len(my_list)):
        my_list.reverse()
        print("{:d}".format(my_list[i]))
