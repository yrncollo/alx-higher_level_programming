#!/usr/bin/python3
"""
This is the "5-text_indentation" module.

The "5-text_indentation" module supplies one function, text_indentation(text).
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: ., ? and :
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    space = 0
    for char in text:
        if space == 0:
            if char == ' ':
                continue
            else:
                space = 1
        if space == 1:
            if char == '.' or char == '?' or char == ':':
                print(char)
                print()
                space = 0
            else:
                print(char, end="")
