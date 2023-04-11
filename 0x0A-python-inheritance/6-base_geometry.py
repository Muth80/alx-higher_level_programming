#!/usr/bin/python3
"""Module with BaseGeometry class."""


class BaseGeometry:
    """
    Class with area method.

    Methods:
        area(self): raises an Exception with the message
        area() is not implemented
    """

    def area(self):
        """Raise an exception with a message."""
        raise Exception("area() is not implemented")

