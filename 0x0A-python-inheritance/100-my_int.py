#!/usr/bin/python3

class MyInt(int):
    """Class MyInt that inherits from int.

    MyInt is a rebel. MyInt has == and != operators inverted.
    """

    def __eq__(self, other):
        """Override the == operator to invert its behavior."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override the != operator to invert its behavior."""
        return super().__eq__(other)

