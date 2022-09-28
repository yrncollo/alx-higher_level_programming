#!/usr/bin/python3
"""
"101-add_attribute" module supplies one function, add_attribute
"""


def add_attribute(obj, name, value):
    """
    adds a new attribute to an object
    """
    if ('__dict__' in dir(obj)):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
