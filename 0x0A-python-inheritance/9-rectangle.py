#!/usr/bin/python3
"""
    9-rectangle: class Rectangle from BaseGeomerty
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        Rectangle inherits from BaseGeometry
        Attributes:
            width (int): width of the rectangle
            height (int): height of the rectangle
        Methods:
            __init__ - initializes the rectangle.
    """
    def __init__(self, width, height):
        """
            initializes Rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """
            Returns the area of a rectangle
        """
        area = self.__width * self.__height
        return area

    def __str__(self):
        """
            retruns rectangle properties
        """
        return ("[{}] {}/{}".format(type(self).__name__,
                                    self.__width, self.__height))
