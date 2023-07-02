#!/usr/bin/python3
"""
A script that takes in a URL and sends a request to it, and then displays the
body of the response
"""
import requests
import sys


if __name__ == '__main__':
    r = requests.get(sys.argv[1])
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
