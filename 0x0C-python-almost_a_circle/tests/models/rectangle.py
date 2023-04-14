#!/usr/bin/python3
""" Module for Rectangle class """

class Rectangle:
    """ A Rectangle class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes an instance of the Rectangle class """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        if id is None:
            Rectangle.count += 1
            self.id = Rectangle.count
        else:
            self.id = id

    def area(self):
        """ Returns the area of the Rectangle """
        return self.width * self.height

    def display(self):
        """ Prints the Rectangle with '#' characters """
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """ Returns a string representation of the Rectangle """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args):
        """ Assigns an argument to each attribute of the Rectangle """
        attributes = ["id", "width", "height", "x", "y"]
        for i, arg in enumerate(args):
            setattr(self, attributes[i], arg)

