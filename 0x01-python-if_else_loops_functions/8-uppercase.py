#!/usr/bin/python3
# 8-uppercase.py

def uppercase(str):
    """Print a string in uppercase."""
    uppercase_string = ""
    for c in str:
         if ord(c) >= 97 and ord(c) <= 122:
             c = chr(ord(c) - 32)
        uppercase_string += c
        print(uppercase_string)
        return uppercase_string
