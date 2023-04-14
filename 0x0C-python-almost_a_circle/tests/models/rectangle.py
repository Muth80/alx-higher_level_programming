#!/usr/bin/python3
"""
Module containing the Rectangle class
"""


class Rectangle:
    """
    Rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle instance"""
        self.id = id
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """Return the area of the Rectangle instance"""
        return self.width * self.height

    @property
    def width(self):
        """Getter method for the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for the width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter method for the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for the height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """Getter method for the x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method for the x attribute"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """Getter method for the y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter method for the y attribute"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value
