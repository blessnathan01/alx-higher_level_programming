#!/usr/bin/python3
""" Module contains: class Square """


class Square():
    """
        Square: defines a square
        Attributes:
            size (no type or value identification): square's size
        Method:
                __init__ : init of size attribute for each instance
    """

    def __init__(self, size):

        """ Initialization of attributes for instances
            Args:
                size (no type): square's size
        """
        self.__size = size
