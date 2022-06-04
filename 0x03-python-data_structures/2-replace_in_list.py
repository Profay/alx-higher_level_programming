#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    a = len(my_list) - 1
    if idx >= 0 and idx <= a:
        my_list[idx] = element
        return my_list
    else:
        return my_list

print(replace_in_list([1, 2, 3, 4, 5], 45, 9))