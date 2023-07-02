#!/usr/bin/python3
"""
A script that takes a set of GitHub credentials and uses the GitHub API to
display the account id
"""
import sys
import requests


if __name__ == '__main__':
    url = "https://api.github.com/users/{}".format(sys.argv[1])
    r = requests.get(url, headers={'Authorization': sys.argv[2]})

    if r.status_code == 200:
        fields = r.json()
        print(fields.get('id'))
    else:
        print(None)
