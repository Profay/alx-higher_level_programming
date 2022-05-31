#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0:
        part = str[:n]
        parts = str[n+1:]
        return part + parts
    else:
        return str
