#!/usr/bin/python3
"""Module that contains the Student class"""


class Student:
    """
    Defines a student by their first name, last name, and age.

    Public instance attributes:
    - first_name
    - last_name
    - age
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student object with the given first name,
        last name, and age.

        Args:
        - first_name (str): the first name of the student
        - last_name (str): the last name of the student
        - age (int): the age of the student
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        If attrs is a list of strings, only the attributes with names
        in this list are retrieved. Otherwise, all attributes are
        retrieved.

        Args:
        - attrs (list of str): a list of attribute names to retrieve

        Returns:
        - A dictionary representation of the Student instance
        """

        if attrs is not None and not isinstance(attrs, list):
            raise TypeError("attrs must be a list of strings")

        if attrs is None:
            return self.__dict__

        filtered_dict = {}
        for attr in attrs:
            if not isinstance(attr, str):
                raise TypeError("attrs must be a list of strings")
            if attr in self.__dict__:
                filtered_dict[attr] = self.__dict__[attr]
        return filtered_dict

