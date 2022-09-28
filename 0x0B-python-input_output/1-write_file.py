#!/usr/bin/python3
"""
This module supplies one function, "write_file"
"""


def write_file(filename="", text=""):
    """returns the number of chars of the string written to "filename"
    from "text" """
    with open(filename, 'w', encoding='utf=8') as f:
        return f.write(text)
