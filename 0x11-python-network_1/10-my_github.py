#!/usr/bin/python3
"""
A script that takes a set of GitHub credentials and uses the GitHub API to
display the account id
"""
import sys
import requests


if __name__ == '__main__':
    url = "https://api.github.com/user"
    r = requests.get(
        url,
        auth=requests.auth.HTTPBasicAuth(sys.argv[1], sys.argv[2])
    )

    if r.status_code == 200:
        fields = r.json()
        print(fields.get('id'))
    else:
        print(None)
