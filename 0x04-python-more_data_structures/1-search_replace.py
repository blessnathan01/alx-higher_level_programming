#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list2 = []
    for x in my_list:
        if x == search:
            list2.append(replace)
        else:
            list2.append(x)
    return list2

