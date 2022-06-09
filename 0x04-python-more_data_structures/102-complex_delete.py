#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    key_list = []
    if value in a_dictionary.values():
        for k, v in a_dictionary.items():
            if value == v:
                key_list.append(k)

        for k2 in key_list:
            if k2 in a_dictionary:
                del a_dictionary[k2]
    return a_dictionary
