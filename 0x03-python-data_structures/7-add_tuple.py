#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a, b = 0, 0
    for tup in (tuple_a, tuple_b):
        if len(tup) > 0:
            a += tup[0]
        if len(tup) > 1:
            b += tup[1]
    return a, b
