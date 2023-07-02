#!/usr/bin/python3
"""
A script that send as POST request to a passed URL with the passed in email as
a parameter, and finally displays the body of the response
"""
import requests
import sys


if __name__ == '__main__':
    r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(r.text)
