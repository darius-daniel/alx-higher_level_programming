#!/usr/bin/python3

def remove_char_at(str, n):
    if n < 0:
        n = len(str) - 1 - n
    i = 0
    new_str = ""
    for ch in str:
        if i != n:
            new_str = new_str + ch
        i += 1
    return new_str
