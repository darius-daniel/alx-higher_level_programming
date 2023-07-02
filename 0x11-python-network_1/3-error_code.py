#!/usr/bin/python3
"""
A Python script that takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8)
"""
from urllib import error, request
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    req = request.Request(url)
    try:
        trial = request.urlopen(req)
    except error.HTTPError as e:
        print("Error Code: {}".format(e.code))
    else:
        trial.close()
        with request.urlopen(url) as response:
            content = response.read()
            print(content)
