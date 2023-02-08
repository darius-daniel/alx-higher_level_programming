#!/usr/bin/python3

"""A function that opens a file, reads it contents and prints it to stdout.

Prototype: def read_file(filename=""):
    filename: the file to be read
"""


def read_file(filename=""):
    """Reads the contents of a file and prints it to stdout

    Args:
        filename = a string containing the path and name of the file
    """
    if filename:
        with open(filename, 'r') as file:
            for line in file:
                print(line, end='')
