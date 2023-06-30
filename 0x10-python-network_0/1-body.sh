#!/bin/bash
# A script to display the body of the response
curl -s -w"%{http_code}" "$1"
