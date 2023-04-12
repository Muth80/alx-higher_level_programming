#!/usr/bin/python3
"""
This module defines read_file function
"""

def read_file(filename=""):
    """Reads a text file and prints it to stdout.

    Args:
        filename (str): The name of the file to read.

    Returns:
        None
    """
    with open(filename, mode='r', encoding='utf-8') as f:
        print(f.read(), end="")


