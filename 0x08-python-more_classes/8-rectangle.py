#!/usr/bin/python3
"""
Module for Rectangle class
"""


class Rectangle:
    """
    Defines a rectangle with a width and height
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle with a given width and height"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter method for the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter method for the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Return the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return a string representation of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return ((str(self.print_symbol) * self.__width + '\n') *
                self.__height).strip()

    def __repr__(self):
        """Return a string representation of the rectangle that can be used to recreate it"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Delete the rectangle and print a message"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

