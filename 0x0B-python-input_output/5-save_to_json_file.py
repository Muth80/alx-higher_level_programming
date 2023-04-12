#!/usr/bin/python3
"""Module to save an object as JSON to a file"""

import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation"""
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)

