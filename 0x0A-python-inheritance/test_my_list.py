#!/usr/bin/python3
"""
Tests for MyList class in 1-my_list.py module.
"""

import os
import sys
import unittest

sys.path.append(os.getcwd())

from my_list import MyList

class TestMyList(unittest.TestCase):
    """
    Tests for MyList class.
    """

    def test_print_sorted(self):
        """
        Test print_sorted method of MyList class.
        """
        my_list = MyList([1, 4, 2, 3, 5])
        sorted_list = [1, 2, 3, 4, 5]
        my_list.print_sorted()
        self.assertEqual(my_list, sorted_list)

if __name__ == '__main__':
    unittest.main()

