#!/usr/bin/python3

"""Contains a function that divides the elements of a matrix.
Each row of the matrix must have the same size.

Prototype: def matrix_divided(matrix, div):
    matrix: must be a list of lists of integers or floats.
    div: must be a number (integer or float), it is the number by which
         all the elements of the matrix should be divided
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix

    Args:
        matrix: a list containing lists of integers or floats.
        div: the number by which all the elements of the matrix will be
        divided by. It must be a number (integer or float)

    Returns:
        list: a new matrix
    """
    if type(div) != float and type(div) != int:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    msg = "matrix must be a matrix (list of lists) of integers/floats"
    for row in matrix:
        if type(row) != list:
            raise TypeError(msg)

    temp = list(filter(lambda item: len(item) == len(matrix[0]), matrix))
    if len(temp) != len(matrix):
        raise TypeError("Each row of the matrix must have the same size")

    new_matrix = []
    for row in matrix:
        sub_list = []
        for num in row:
            if type(num) != float and type(num) != int:
                raise TypeError(msg)
            else:
                sub_list.append(float("{:.2f}".format(num / div)))

        new_matrix.append(sub_list)

    return new_matrix
