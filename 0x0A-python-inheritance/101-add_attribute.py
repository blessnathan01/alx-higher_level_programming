#!/usr/bin/python3
"""
    101-add_attribute: add_attribute()
"""


def add_attribute(attr, name, value):
    """
        adds a brand new attribute to an object
    """
    if hasattr(attr, "__dict__") is False:
        raise TypeError("can't add new attribute")
    setattr(attr, name, value)
