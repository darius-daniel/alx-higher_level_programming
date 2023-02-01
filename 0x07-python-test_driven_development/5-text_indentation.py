#!/usr/bin/python3

"""Contains a function that prints a text with 2 new lines after each of
of these characters: '.', '?' and ':'

Prototype: def text_indentation(text):
    text: must be a string (otherwise raise a TypeError)

There should be no space at the beginning or at the end of each printed line
"""


def text_indentation(text):
    """A function that prints a text with 2 new lines after each of the
    following characters: '.', '?', ':'

    Args:
        text: a string
    """
    if type(text) != str:
        raise TypeError("text must be a string")

    special_chars = ".?:"
    i = 0
    for ch in text:
        if i > len(text) - 1:
            break
        print(text[i], end='')
        if text[i] in special_chars and i < len(text) - 1:
            print("\n")
            if i == len(text) - 1:
                break
            elif text[i + 1] == ' ':
                i += 1
        i += 1
    print()
