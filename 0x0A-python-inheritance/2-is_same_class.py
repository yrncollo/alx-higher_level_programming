#!/usr/bin/python3
"""
"2-is_same_class" module supplies one function, is_same_class
"""


def is_same_class(obj, a_class):
    """return true if object is exactly an instance of the specified
    class, otherwise false"""
    return (type(obj) == a_class)
