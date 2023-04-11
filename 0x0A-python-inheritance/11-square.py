#!/usr/bin/python3
"""Module documentation"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """Square constructor"""
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """String representation of Square"""
        return "[Square] {}/{}".format(self.__size, self.__size)

    def area(self):
        """Calculate the area of the Square"""
        return self.__size ** 2

