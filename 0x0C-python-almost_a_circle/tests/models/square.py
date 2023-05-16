#!/usr/bin/python3
"""Define a Square class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return a string representation of the square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        """Get the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the square"""
        attrs = ["id", "size", "x", "y"]
        if args:
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                if key in attrs:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return a dictionary representation of the square"""
        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}

