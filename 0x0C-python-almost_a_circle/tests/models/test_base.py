#!/usr/bin/python3
"""
This module contains the unit tests for the Base class
"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Test cases for the Base class
    """

    def test_id(self):
        """
        Test that each instance has a unique id
        """
        b1 = Base()
        b2 = Base()
        b3 = Base(12)
        b4 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 12)
        self.assertEqual(b4.id, 3)


if __name__ == "__main__":
    unittest.main()

