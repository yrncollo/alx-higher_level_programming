#!/usr/bin/python3
"""Defines Lazy matrix multiplication using Numpy module
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """ multiplies two matrices"""
    return numpy.matmul(m_a, m_b)
