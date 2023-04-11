#!/usr/bin/python3
"""Module that defines a square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""

    def __init__(self, size):
        """Initialize a new Square instance"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return a string representation of the square"""

        return "[Square] {}/{}".format(self.__size, self.__size)

