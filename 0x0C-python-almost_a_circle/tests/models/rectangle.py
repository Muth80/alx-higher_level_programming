#!/usr/bin/python3
"""Module that contains a rectangle"""

class Rectangle(Base):
    """Class that represents a rectangle."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor method."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter method for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width."""
        self.integer_validator("width", value)
        self.__width = value

    @property
    def height(self):
        """Getter method for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height."""
        self.integer_validator("height", value)
        self.__height = value

    @property
    def x(self):
        """Getter method for x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method for x."""
        self.integer_validator("x", value)
        self.__x = value

    @property
    def y(self):
        """Getter method for y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter method for y."""
        self.integer_validator("y", value)
        self.__y = value

    def area(self):
        """Method that returns the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Method that prints in stdout the Rectangle instance with the character #."""
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        """Method that returns a string representation of the Rectangle instance."""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Method that updates the attributes of the Rectangle instance."""
        attrs = ["id", "width", "height", "x", "y"]
        if args:
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for k, v in kwargs.items():
                if k in attrs:
                    setattr(self, k, v)

    def to_dictionary(self):
        """Method that returns the dictionary representation of a Rectangle instance."""
        return {"id": self.id, "width": self.width, "height": self.height, "x": self.x, "y": self.y}

