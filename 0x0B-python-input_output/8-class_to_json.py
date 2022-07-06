#!/usr/bin/python3
"""
    8-class_to_json: class_to_json()
"""


def class_to_json(obj):
    """
        returns a dictionary details with simple data structure
    """
    return obj.__dict__
