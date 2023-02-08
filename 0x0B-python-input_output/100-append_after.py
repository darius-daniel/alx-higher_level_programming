#!/usr/bin/python3

"""Contains a function that inserts a line of text to a file, after each line
containing a specific string

Prototype: def append_after(filename="", search_string="", new_string=""):
    filename: string containing the file to be read
    search_string: the specified string
    new_string: the inserted string
"""


def append_after(filename="", search_string="", new_string=""):
    """Contains a function that inserts a line of text to a file, after each
    line containing a specific string

    Args:
        filename: string containing the file to be read
        search_string: the specified string
        new_string: the inserted string
    """
    line_list = []
    with open(filename, 'r', encoding="utf-8") as file:
        for line in file:
            line_list.append(line)
            if line.find(search_string) != -1:
                line_list.append(new_string)

    with open(filename, 'w', encoding="utf-8") as file:
        file.write("".join(line_list))
