#!/usr/bin/python3

def uppercase(str):
    lower_chars = 'abcdefghijklmnopqrstuvwxyz'
    upper_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    end_str, i = '', 0

    if ch == '':
        print("{}".format('\n'))
    for ch in str:
        if i == len(str) - 1:
            end_str = '\n'

        if ch in lower_chars:
            print("{}".format(upper_chars[lower_chars.find(ch)]), end=end_str)
        else:
            print("{}".format(ch), end=end_str)

        i += 1
