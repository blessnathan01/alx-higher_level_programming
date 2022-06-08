#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # create a set with non-common elements from given sets
    set_3 = set_1 ^ set_2
    return set_3
