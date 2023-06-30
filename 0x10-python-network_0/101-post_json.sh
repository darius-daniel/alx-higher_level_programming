#!/bin/bash
# A Bash script that sends a JSON file as a POST request and displays the body of the response
curl -s -d "@$2" -X POST -H "Content-Type: application/json" "$1"
