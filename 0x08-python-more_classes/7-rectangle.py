#!/usr/bin/python3
"""Module containing the Rectangle class"""


class Rectangle:
    """Rectangle class with width, height, area, and perimeter attributes"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance with the given width and height"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __str__(self):
        """Return a string representation of the Rectangle instance"""
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(str(self.print_symbol) * self.width for i in range(self.height))

    def __repr__(self):
        """Return a string representation of the Rectangle instance
        that can be used to recreate the instance"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Print a message when a Rectangle instance is deleted"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        """Return the width of the Rectangle instance"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the Rectangle instance to the given value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Return the height of the Rectangle instance"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the Rectangle instance to the given value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle instance"""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the Rectangle instance"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

