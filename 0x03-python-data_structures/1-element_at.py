#!/usr/bin/python3

def element_at(my_list, idx):
    a = len(my_list) - 1
    if idx >= 0 and idx <= a:
        print("Element at index {:d} is {}".format(idx, my_list[idx]))
    else:
        print("None")
