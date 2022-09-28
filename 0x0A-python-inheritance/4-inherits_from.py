#!/usr/bin/python3
"""
"4-inherits_from" module supplies one function, inherits_from function
"""


def inherits_from(obj, a_class):
    """returns true if object is an instance of a class that inherited
    from the specifid class, otherwise false"""
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
