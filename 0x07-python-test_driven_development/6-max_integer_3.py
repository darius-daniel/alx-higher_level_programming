#!/usr/bin/python3

"""DocString

Prototype: def max_integer(list=[]):
                pass
"""


def max_integer(list=[]):
    """Doc String

    Args:
        list: the list
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]

    # if middle element => find another integer
    if list[0] != result and list[-1] != result and len(list) > 2:
        old_result = result
        result = list[0]
        i = 1
        while i < len(list):
            if list[i] != old_result:
                result = list[i]
                break

            i += 1

    return  result
