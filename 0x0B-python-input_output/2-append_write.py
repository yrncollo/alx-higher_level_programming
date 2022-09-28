#!/usr/bin/python3
"""
Module supplies the function, append_write
"""


def append_write(filename="", text=""):
    """returns the number of chars of the string added to "filename"
    from "text" """
    with open(filename, 'a', encoding='utf=8') as f:
        return f.write(text)
