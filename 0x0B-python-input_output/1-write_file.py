#!/usr/bin/python3

"""Contains a function that writes a string to a text file

Prototype: def write_file(filename="", text="")
    filename = a string containing the path and name of the file
    text = a string containing the text to be written to the file
"""


def write_file(filename="", text=""):
    """Writes a string to a text file and returns the number of characters
    written

    Args:
        filename: a string containing the name and/or name of the file
        text:
    """
    nb_chars = 0
    if filename:
        with open(filename, 'w') as file:
            nb_chars = file.write(text)
    return nb_chars
