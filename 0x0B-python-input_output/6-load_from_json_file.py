#!/usr/bin/python3

# This is a comment explaining the purpose of the file

import json

class InvalidJsonDataError(Exception):
    pass

def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename (str): The filename of the JSON file.

    Returns:
        object: The object represented by the JSON data in the file.

    Raises:
        FileNotFoundError: If the file is not found.
        InvalidJsonDataError: If the JSON data is invalid.

    """
    try:
        with open(filename, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except json.JSONDecodeError:
        raise InvalidJsonDataError(f"Invalid JSON data in '{filename}'.")

    return data

if __name__ == '__main__':
    filename = "my_list.json"
    my_list = load_from_json_file(filename)
    print(my_list)
    print(type(my_list))

    filename = "my_dict.json"
    my_dict = load_from_json_file(filename)
    print(my_dict)
    print(type(my_dict))

    try:
        filename = "my_set_doesnt_exist.json"
        my_set = load_from_json_file(filename)
        print(my_set)
        print(type(my_set))
    except FileNotFoundError as e:
        print(f"[{type(e).__name__}] {e}")

    try:
        filename = "my_fake.json"
        my_fake = load_from_json_file(filename)
        print(my_fake)
        print(type(my_fake))
    except InvalidJsonDataError as e:
        print(f"[{type(e).__name__}] {e}")

