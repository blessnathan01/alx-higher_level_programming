#!/usr/bin/python3
"""
    1-my_list: class MyList
"""


class MyList(list):
    """
        This class inherits from a list
        Attributes:
        Methods:
            print_sorted - prints a sorted list
    """
    def print_sorted(self):
        """
           prints a list in ascending order
        """
        print(sorted(self))
