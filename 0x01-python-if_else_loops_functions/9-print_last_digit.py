#!/usr/bin/python3

def print_last_digit(number):
    if number < 0:
        result = -number % 10
    else:
        result = number % 10
    print("{d}".format(result), end='')
    return number % 10
