#!/usr/bin/python3

"""Contains a function that appends a string at the end of a text file and
returns the number or characters added

Prototype: def append_write(filename="", text=""):
    filename: a string that contains the path and name of the file to be
              appended to
    text: a string containing the text to be appended to the file
"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file and returns the number of
    characters added
    """
    nb_chars = 0
    if filename:
        with open(filename, 'a') as file:
            nb_chars = file.write(text)
    return nb_chars
