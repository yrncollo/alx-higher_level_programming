#!/usr/bin/python3
"""The "101-locked_class" module
This module supplies one class, LockedClass
"""


class LockedClass:
    """Locked class that pevents the user from dynamically creating new
    instance attributes except if the new instance variable is called
    first_time"""
    __slots__ = ['first_name']
