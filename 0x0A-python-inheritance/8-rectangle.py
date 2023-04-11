#!/usr/bin/python3
"""
This module defines a BaseGeometry class and a Rectangle class that inherits
from it.
"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Calculate the area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate an integer value"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """Initialize a new Rectangle instance"""
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Return a string representation of the Rectangle instance"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """Calculate the area of the Rectangle instance"""
        return self.__width * self.__height

    @property
    def width(self):
        """Return the width of the Rectangle instance"""
        return self.__width

    @property
    def height(self):
        """Return the height of the Rectangle instance"""
        return self.__height

