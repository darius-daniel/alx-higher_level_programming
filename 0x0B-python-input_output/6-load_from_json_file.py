#!/usr/bin/python3
import json

def load_from_json_file(filename):
    if filename:
        with open(filename, "r", encoding="utf-8") as file:
            obj = json.load(file)
        return obj
