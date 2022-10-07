#!/usr/bin/python3
"""Rectangle module which inherits from Base"""
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
