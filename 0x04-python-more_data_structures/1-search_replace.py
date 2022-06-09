#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list2 = []
    for x in range(len(my_list)):
        if my_list[x] == search:
            list2.append(replace)
        else:
            list2.append(my_list[x])
    return list2
