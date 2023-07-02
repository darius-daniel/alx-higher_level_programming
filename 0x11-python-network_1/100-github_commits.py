#!/usr/bin/python3
"""
A python script to solve the advanced task
"""
import requests
import sys


if __name__ == '__main__':
    url = "https://api.github.com/users/{}/hovercard?subject_type=repository".format(sys.argv[1])
    r = requests.get(url, headers={})
