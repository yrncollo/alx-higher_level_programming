#!/usr/bin/python3
"""Module to multiply two matrices
"""


def matrix_mul(m_a, m_b):
    """Function that multiplies two matrices
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    m_a_size = 0
    for row in m_a:
        if type(row) is not list:
            raise TypeError("m_a must be a list of lists")
        if len(row) == 0:
            raise ValueError("m_a can't be empty")
        m_a_size = len(row)
        if m_a_size != len(row):
            raise TypeError("each row of m_a must should be of the same size")
        for column in row:
            if type(column) is not int and type(column) is not float:
                raise TypeError("m_a should contain only integers or floats")
    m_b_size = 0
    for row in m_b:
        if type(row) is not list:
            raise TypeError("m_b must be a list of lists")
        if len(row) == 0:
            raise ValueError("m_b can't be empty")
        m_b_size = len(row)
        if m_b_size != len(row):
            raise TypeError("each row of m_b must should be of the same size")
        for column in row:
            if type(column) is not int and type(column) is not float:
                raise TypeError("m_b should contain only integers or floats")
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    if m_a_size != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    matrix = []
    for i in range(len(m_a)):
        new = []
        for j in range(m_b_size):
            n = 0
            for k in range(m_a_size):
                n += m_a[i][k] * m_b[k][j]
            new.append(n)
        matrix.append(new)
    return matrix
