#!/usr/bin/python3
"""
    7-base_geometry: class BaseGeometry
"""


class BaseGeometry:
    """
        BaseGeometry
        Attributes: None
        Methods:
            area() - raises an exception
            integer_validator() - validates a value
    """
    def area(self):
        """
            Area raise an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            integer_validator validates the value
            Args:
                name (str): name
                value (int): value
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
