#!/usr/bin/python3

"""Contains a function that multiplies to matrices:

Prototype: def matrix_mul(m_a, m_b):

Args:
    m_a: must be a list of lists of integers 
    m_b: must also be a list of lists of integers
"""


def matrix_mul(m_a, m_b):
    """Computes the product of two matrices m_a and m_b

    Args:
        m_a: the first matrix to be multiplied
        m_b: the second matrix

    Returns:
        another matrix (the cross product of the two input matrices)
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    for obj in m_a:
        if not isinstance(obj, list):
            raise TypeError("m_a must be a list of lists")
    for obj in m_b:
        if not isinstance(obj, list):
            raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")

    for objs in m_a:
        for obj in objs:
            if not isinstance(obj, int) and not isinstance(obj, float):
                raise TypeError("m_a should contain only integers or floats")

    for objs in m_b:
        for obj in objs:
            if not isinstance(obj, int) and not isinstance(obj, float):
                raise TypeError("m_b should contain only integers or floats")

    filtered_list = list(filter(lambda row: len(row) == len(m_a[0]), m_a))
    if len(filtered_list) != len(m_a):
        raise TypeError("each row of m_a must be of the same size")

    filtered_list = list(filter(lambda row: len(row) == len(m_a[0]), m_b))
    if len(filtered_list) != len(m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    row_1 = []
    num_1 = 0

    for row in m_a:
        row_2 = []
        num_2 = 0
        num = 0
        while (num_2 < len(m_b[0])):
            num += row[num_1] * m_b[num_1][num_2]
            if num_1 == len(m_b) - 1:
                num_1 = 0
                num_2 += 1
                row_2.append(num)
                num = 0
            else:
                num_1 += 1
        row_1.append(row_2)

    return row_1
