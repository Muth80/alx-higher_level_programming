#!/usr/bin/python3

# This script defines a function that loads a JSON object from a file.

import json

def load_from_json_file(filename):
    """
    Load a JSON object from a file.

    Args:
        filename (str): The name of the JSON file.

    Returns:
        dict: The deserialized JSON object.

    """
    with open(filename) as f:
        data = json.load(f)
    return data

