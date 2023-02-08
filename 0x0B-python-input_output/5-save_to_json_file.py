#!/usr/bin/python3
from json import dump
def save_to_json_file(my_obj, filename):
    if filename:
        with open(filename, 'w', encoding="utf-8") as file:
            dump(my_obj, file)
