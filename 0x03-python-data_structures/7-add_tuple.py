#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    return list(map(lambda x, y: x + y, tuple_a, tuple_b))
