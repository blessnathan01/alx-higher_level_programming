#!/usr/bin/python3
""" Module 3-square: class Square """


class Square():
    """
        Square: square definition
        Attributes:
            size (int): square's size
        Method:
                __init__ : init of size attribute for each instance
    """

    def __init__(self, size=0):

        """ Initialization of attributes for instances
            Args:
                size (int): square's size
        """
        if (isinstance(size, int)):
            self.__size = size
            if size < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        return self.__size ** 2
