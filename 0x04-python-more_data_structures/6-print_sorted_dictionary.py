#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dict = sorted(a_dictionary.keys())
    for x in sorted_dict:
        print("{:s}: {}".format(x, a_dictionary[x]))
