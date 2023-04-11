#!/usr/bin/python3
"""
Module 7-base_geometry

A module that contains a BaseGeometry class
with area and integer_validator methods
"""


class BaseGeometry:
    """
    A class that contains area and integer_validator methods
    """

    def area(self):
        """
        Method that raises an Exception with the message area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Method that validates value:
        Args:
            name (str): name of the variable
            value (int): integer value to validate
        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

