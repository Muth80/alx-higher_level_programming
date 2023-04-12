#!/usr/bin/python3

def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns the number of characters written.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text to write to the file.

    Returns:
        The number of characters written to the file.
    """
    with open(filename, mode='w', encoding='utf8') as file:
        return file.write(text)

