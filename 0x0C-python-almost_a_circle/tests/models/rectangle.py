#!/usr/bin/python3
"""Module that contains a Square class that inherits from Rectangle class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a square instance"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns a string representation of the square"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Getter method for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter method for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the square attributes"""
        if args:
            attrs = ["id", "size", "x", "y"]
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        else:
            for attr, value in kwargs.items():
                setattr(self, attr, value)

    def to_dictionary(self):
        """Returns the dictionary representation of the square"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}

