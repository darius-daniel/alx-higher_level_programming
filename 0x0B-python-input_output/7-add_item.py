#!/usr/bin/python3
"""A script that adds all arguments to a Python list and then save them to a
file
"""
import sys
import os.path


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

file = 'add_item.json'
args = []
if os.path.exists(file):
    args = load_from_json_file(file)

for arg in sys.argv[1:]:
    args.append(arg)

save_to_json_file(sys.argv[1:], file)
