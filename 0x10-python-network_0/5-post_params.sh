#!/bin/bash
# A script that displays the body of the response to a POST request
curl -s -H "email: test@gmail.com" -d "subject: I will always be here for PLD" -d POST "$1"
