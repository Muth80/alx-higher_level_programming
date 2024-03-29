#!/usr/bin/python3
"""Module containing Student class"""


class Student:
    """Represents a student"""

    def __init__(self, first_name, last_name, age):
        """Instantiates a new student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance"""
        return self.__dict__.copy()

