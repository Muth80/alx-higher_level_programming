#!/usr/bin/python3
"""
Module containing is_same_class and is_kind_of_class functions
"""


def is_same_class(obj, a_class):
    """
    Returns True if obj is exactly an instance of a_class; False otherwise
    """
    return type(obj) is a_class


def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is an instance of a_class or an instance of a subclass of a_class; False otherwise
    """
    return isinstance(obj, a_class)

