#!/usr/bin/python3
""" A script with a function that finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
    A function that finds a peak in a list of unsorted integers
    """
    if len(list_of_integers) > 0:
        peak = list_of_integers[0]
        for i in list_of_integers[0:]:
            if i > peak:
                peak = i

        return peak
