#!/usr/bin/python3
"""
A python script to solve the advanced task
"""
import requests
import sys


if __name__ == '__main__':
    url = "https://api.github.com/repos/"
    url = "{}{}/{}/commits".format(url, sys.argv[2], sys.argv[1])
    r = requests.get(url)
    commits = r.json()

    i = 0
    for commit in commits:
        if i == 10:
            break
        sha = commit.get('sha')
        author = commit.get('commit').get('author').get('name')
        print("{}: {}".format(sha, author))
        i += 1
