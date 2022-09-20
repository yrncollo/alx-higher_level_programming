#!/usr/bin/python3
"""
This is the "2-matrix_divided" module.

The "2-matrix_divided" module  supplies one function,
    matrix_divided(mtrix, div).
"""


def matrix_divided(matrix, div):
    """
    Returns a new matrix comprised of elements of a matrix divided by number
    """
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers\
/floats")
    size = None
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
        if size is None:
            size = len(row)
        elif size != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        for column in row:
            if type(column) is not int and type(column) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(column / div, 2) for column in row] for row in matrix]
