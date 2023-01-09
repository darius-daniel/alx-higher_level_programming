#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence == '':
        f_ch = None
    else:
        f_ch = sentence[0]

    return (len(sentence), f_ch)
