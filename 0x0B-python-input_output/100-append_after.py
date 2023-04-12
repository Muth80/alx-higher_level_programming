#!/usr/bin/python3
"""
Module for append_after method
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file, after each line containing a specific string

    Args:
        filename (str): name of the file to append to
        search_string (str): string to search for in file
        new_string (str): string to append after each line containing search_string

    Returns:
        None
    """

    with open(filename, mode="r+", encoding="utf-8") as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
        f.truncate()


