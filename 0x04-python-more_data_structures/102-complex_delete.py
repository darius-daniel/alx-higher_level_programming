#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    key_dict = [
        key
        for key in a_dictionary.keys()
        if a_dictionary[key] == value
        ]

    for key in key_dict:
        del a_dictionary[key]
    return a_dictionary
