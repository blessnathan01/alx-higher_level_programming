#!/usr/bin/python3
"""
    0-lookup: lookup()
"""


def lookup(obj):
    """
        Returns the list of available object methods & attributes
        Args:
            obj (object): object.
    """
    return (dir(obj))
