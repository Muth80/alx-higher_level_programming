#!/usr/bin/python3
"""
Module for lookup and is_same_class functions.
"""


def lookup(obj):
    """Returns the list of available attributes and methods of an object."""
    return dir(obj)


def is_same_class(obj, a_class):
    """Returns True if the object is exactly an instance of the specified class ; otherwise False."""
    return type(obj) is a_class

