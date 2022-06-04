#!/usr/bin/python3

def no_c_print(s):
    new_string = ''
    for character in s:
        if character not in 'Cceat':
            new_string += character
    print(new_string)


no_c_print("Characters")