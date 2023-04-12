#!/usr/bin/python3
"""Adds all arguments to a Python list and saves them to a file."""

import sys
import json
from os import path
from typing import List
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if __name__ == '__main__':
    file_path = "add_item.json"
    my_list: List[str] = []
    if path.exists(file_path):
        my_list = load_from_json_file(file_path)

    my_list.extend(sys.argv[1:])
    save_to_json_file(my_list, file_path)

