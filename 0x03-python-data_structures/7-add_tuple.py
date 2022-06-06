#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    lenA = len(tuple_a)
    lenB = len(tuple_b)

    if lenA == 0:
        x1 = 0
        x2 = 0
    elif lenA == 1:
        x1 = tuple_a[0]
        x2 = 0
    else:
        x1 = tuple_a[0]
        x2 = tuple_a[1]

    if lenB == 0:
        y1 = 0
        y2 = 0
    elif lenB == 1:
        y1 = tuple_b[0]
        y2 = 0
    else:
        y1 = tuple_b[0]
        y2 = tuple_b[1]

    tuple_c = x1+y1, x2+y2
    return tuple_c
