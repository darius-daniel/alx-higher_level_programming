#!/usr/bin/python3
"""Contains a function that compute the first n rows of the Pascal's triangle

Prototype: def pascal_triangle(n):
    n: the number of rows
"""


def pascal_triangle(n):
    """Computes the first n rows of the Pascal triangle

    Args:
        n: (int)number of rows

    Returns:
        list: a list of all the rows (list)
    """
    if n <= 0:
        return []

    pascal_tri = []
    prev_row = []
    for i in range(n + 1):
        row = [1]
        for j in range(len(prev_row)):
            if j == 0 or j == len(prev_row) - 1:
                row.append(1)
            else:
                row.append(prev_row[j] + prev_row[j + 1])

        pascal_tri.append(row)
        prev_row = row[:]

    for row in pascal_tri:
        row.pop(0)
    pascal_tri.pop(0)

    return pascal_tri
