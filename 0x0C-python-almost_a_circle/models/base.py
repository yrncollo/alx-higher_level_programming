#!/usr/bin/python3
"""This class would be the base of all other class"""


class Base:
    """private class attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

