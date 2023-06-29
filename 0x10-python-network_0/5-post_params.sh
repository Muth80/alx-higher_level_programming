#!/bin/bash
# This script sends a POST request to the given URL with 
# specified parameters and displays the body of the response

url="$1"
email="test@gmail.com"
subject="I will always be here for PLD"

curl -s -X POST -d "email=$email" -d "subject=$subject" "$url"

