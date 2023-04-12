#!/usr/bin/python3
"""
This module defines the Student class.
"""


class Student:
    """
    Represents a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance with the given attributes.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the student instance.

        Args:
            attrs (list[str]): The list of attributes to retrieve. If None,
                retrieves all attributes.

        Returns:
            dict: The dictionary representation of the student instance.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """
        Replaces all attributes of the student instance with those from the
        given dictionary.

        Args:
            json (dict): The dictionary of attributes to set.
        """
        for key, value in json.items():
            setattr(self, key, value)

