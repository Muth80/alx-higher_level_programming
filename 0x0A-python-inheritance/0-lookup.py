#!/usr/bin/python3


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.


    Args:
        obj: an object to inspect.


    Returns:
        A list of strings representing the available attributes and methods of obj.
    """
    return [attr for attr in dir(obj) if not callable(getattr(obj, attr)) or not attr.startswith("__")]

