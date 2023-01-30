#!/usr/bin/python3

"""Contains a function that prints a square with the character #

Prototype: def print_square(size):
    size: is the size length of the square (must be an integer >= 0)
"""


def print_square(size):
    if type(size) != int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise TypeError("size must be >= 0")

    i = 0
    while (i < size):
        print("{}".format("#" * int(size)))
        i += 1
