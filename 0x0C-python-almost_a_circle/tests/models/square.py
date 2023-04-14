#!/usr/bin/python3
""" Module Square """


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Init method"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Getter method for size """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter method for size """
        self.width = value
        self.height = value

    def __str__(self):
        """Return string"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Update attributes"""
        if args:
            attrs = ["id", "size", "x", "y"]
            for idx, val in enumerate(args):
                setattr(self, attrs[idx], val)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """To dictionary"""
        return {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}

