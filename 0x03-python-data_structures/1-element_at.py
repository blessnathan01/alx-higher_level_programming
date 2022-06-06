#!/usr/bin/python3
def element_at(my_list, idx):
    # if index is negative or out of range, return 'None'
    # else return the corresponding element
    if idx < 0 or idx >= len(my_list):
        return
    else:
        return my_list[idx]
