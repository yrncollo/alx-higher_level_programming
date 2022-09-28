#!/usr/bin/python3
"""
"0-lookup" module supplies one function, lookup
"""


def lookup(obj):
    """returns a list of available attributes and methods of an object"""
    return dir(obj)
