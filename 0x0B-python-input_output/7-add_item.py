#!/usr/bin/python3
"""
Script that adds all arguments to a Python list and saves them to a file
"""
import sys
from os import path
from typing import List

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_item(args: List[str], filename: str) -> None:
    """
    Adds all arguments to a Python list and saves them to a file

    Args:
        args (List[str]): List of command line arguments
        filename (str): Name of the file to save the list to
    """
    my_list = []
    if path.exists(filename):
        my_list = load_from_json_file(filename)

    for arg in args:
        my_list.append(arg)

    save_to_json_file(my_list, filename)


if __name__ == '__main__':
    args = sys.argv[1:]
    add_item(args, "add_item.json")

