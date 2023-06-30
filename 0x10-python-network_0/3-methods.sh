#!/bin/bash
# A script that displays all HTTP methods a server will accept
curl -sI -o /dev/null "$1"
