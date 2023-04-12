#!/usr/bin/python3
"""Module for class to JSON conversion"""

def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON serialization of an object.

    Args:
        obj (object): instance of a class

    Returns:
        dictionary description with simple data structure for JSON serialization
    """
    return obj.__dict__

