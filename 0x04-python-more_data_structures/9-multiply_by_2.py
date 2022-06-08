#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dict2 = a_dictionary.copy()
    for x, y in dict2.items():
        dict2[x] = y * 2
    return dict2
