#!/bin/bash
# A script to display the body of the response
curl -s -w"%{200}" -o /dev/null "$1"
