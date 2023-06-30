#!/usr/bin/bash
# A script displays the size of the body of the reponse in bytes
curl -s -w"%{size_download}" -o /dev/null "$1"
