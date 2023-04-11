#!/usr/bin/python3
"""This module defines a function that determines if an object is an instance of a class that
   inherited (directly or indirectly) from the specified class"""


def inherits_from(obj, a_class):
    """
    Determines if an object is an instance of a class that inherited (directly or indirectly)
    from the specified class.

    Args:
        obj (object): The object to check.
        a_class (class): The class to compare against.

    Returns:
        True if obj is an instance of a class that inherited from a_class, False otherwise.
    """
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)

