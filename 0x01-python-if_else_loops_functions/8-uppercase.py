#!/usr/bin/python3

def uppercase(str):
    lower_chars = 'abcdefghijklmnopqrstuvwxyz'
    upper_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    end_str, i = '', 0

    for ch in str:
        if i == len(str) - 1:
            end_str = '\n'

        if ch in lower_chars:
            print(f"{upper_chars[lower_chars.find(ch)]}", end=end_str)
        else:
            print(ch, end=end_str)

        i += 1
