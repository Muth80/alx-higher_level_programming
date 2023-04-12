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

    Raises:
        FileNotFoundError: If the file does not exist.
        JSONDecodeError: If the file contains invalid JSON.

    """
    # Open the file with 'with' statement to ensure it is properly closed when the block is exited
    with open(filename) as f:
        # Use the 'json.load' function to read the contents of the file and deserialize the JSON object
        data = json.load(f)
    # Return the deserialized JSON object (which is assumed to be a dictionary in this case)
    return data

