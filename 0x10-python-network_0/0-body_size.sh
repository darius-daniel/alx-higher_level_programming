#!/usr/bin/bash
# A script displays the size of the body of the reponse in bytes
curl -sI "$1" | grep "Content-Length:" | cut -d " " -f 2
