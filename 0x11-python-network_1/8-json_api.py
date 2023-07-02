#!/usr/bin/python3
"""
A script that takes in a letter and sends a POST request to a URL with the
letter as a parameter
"""
import requests
import sys


if __name__ == '__main__':
    if len(sys.argv) == 1:
        letter = ''
    else:
        letter = sys.argv[1]

    url = "http://0.0.0.0:5000/search_user"
    r = requests.post(url, data={'q': letter})
    try:
        content = r.json()
    except Exception as e:
        print('Not a valid JSON')
    else:
        if not content:
            print("No result")
        else:
            print("[{}] {}".format(content.get('id'), content.get('name')))
