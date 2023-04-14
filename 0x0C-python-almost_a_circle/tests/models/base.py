#!/usr/bin/python3
"""
This module contains the Base class
"""


class Base:
    """
    The Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes an instance of the Base class

        Args:
            id (int): id of the instance, defaults to None

        Returns:
            None
        """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

