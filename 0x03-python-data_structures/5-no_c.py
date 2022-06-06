#!/usr/bin/python3
def no_c(my_string):
    new_str = my_string.translate({ord('C'): ''})
    new_str = new_str.translate({ord('c'): ''})
    return new_str
