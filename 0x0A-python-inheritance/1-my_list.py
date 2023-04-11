#!/usr/bin/python3
"""
Module that defines MyList class.
"""

class MyList(list):
    """
    A subclass of the list class with additional methods.
    """

    def print_sorted(self):
        """
        Prints the list sorted in ascending order.
        """
        sorted_list = sorted(self)
        print(sorted_list)

