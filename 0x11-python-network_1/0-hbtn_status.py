#!/usr/bin/python3
"""
A script that fetches a url
"""
import urllib.request

url = "https://alx-intranet.hbtn.io/status"
with urllib.request.urlopen(url) as response:
    html = response.read()
    print(html)
