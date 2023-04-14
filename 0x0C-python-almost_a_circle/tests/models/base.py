#!/usr/bin/python3
"""
Module for Base class
"""

import json

class Base:
    """
    Base class for all other classes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize object with id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write JSON string representation of list_objs to a file
        """
        filename = cls.__name__ + ".json"
        json_list = []
        if list_objs:
            for obj in list_objs:
                json_list.append(obj.to_dictionary())
        with open(filename, "w", encoding="utf-8") as file:
            file.write(cls.to_json_string(json_list))

    @staticmethod
    def from_json_string(json_string):
        """
        Return the list of the JSON string representation json_string
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Return an instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            return None
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Return a list of instances
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r", encoding="utf-8") as file:
                json_list = cls.from_json_string(file.read())
                instances = []
                for dictionary in json_list:
                    instances.append(cls.create(**dictionary))
                return instances
        except FileNotFoundError:
            return []


