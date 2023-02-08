#!/usr/bin/python3
"""A script that adds all arguments to a Python list and then save them to a
file
"""
import sys
import os.path


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = 'add_item.json'
args = []
if os.path.exists(filename):
    args = load_from_json_file(filename)

args += sys.argv[1:]
save_to_json_file(sys.argv[1:], filename)
