#!/usr/bin/python3
def uniq_add(my_list=[]):
    # create a list with unique elements only i.e a set
    uniq = set(my_list)
    list2 = list(uniq)
    total = 0
    for x in list2:
        total += x
    return total
