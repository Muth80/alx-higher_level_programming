#!/usr/bin/python3

import json

def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename (str): The filename of the JSON file.

    Returns:
        object: The object represented by the JSON data in the file.

    Raises:
        FileNotFoundError: If the file is not found.
        JSONDecodeError: If the JSON data is invalid.

    """
    try:
        with open(filename, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON data in '{filename}'.")
        return None

    return data

