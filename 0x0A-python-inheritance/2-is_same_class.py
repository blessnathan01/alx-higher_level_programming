#!/usr/bin/python3
"""
    2-is_same_class: is_same_class()
"""


def is_same_class(obj, a_class):
    """
        is_same_class returns True if object is exactly \
                an instance of the specified class
        Args:
            obj (object): object to be checked
            a_class (class): class
        Return: False/True
    """
    if type(obj) is a_class:
        return True
    else:
        return False
