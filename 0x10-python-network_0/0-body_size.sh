#!/usr/bin/bash
# A bash script that makes a request to a URL and displays the size of the body of the reponse in bytes
curl -s -w"%{size_download}" -o /dev/null "$1"
