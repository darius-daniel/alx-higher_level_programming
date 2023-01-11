#!/usr/bin/python3

def sq(x):
    return (x ** 2)


def square_matrix_simple(matrix=[]):
    if matrix:
        new_matrix = []
        for row in matrix:
            new_matrix.append([sq(num) for num in row])
        return new_matrix
