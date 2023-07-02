#!/usr/bin/python3
""" A script that sends a POST request to a URL passed as a cmd line argument
with an email (also passed as an argument from the command line) as a
parameter
"""
from urllib import request, parse
import sys


if __name__ == "__main__":
    value = {'email': sys.argv[2]}
    data = parse.urlencode(value).encode("ascii")
    req = request.Request(sys.argv[1], data)
    with request.urlopen(req) as response:
        html = response.read()
        print(html.decode("utf-8"))
