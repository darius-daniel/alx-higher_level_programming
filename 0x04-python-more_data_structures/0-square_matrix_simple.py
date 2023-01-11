#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if matrix:
        new_matrix = []
        sq = lambda x: x ** 2
        for row in matrix:
            new_matrix.append([sq(num) for num in row])
        return new_matrix
