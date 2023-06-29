#!/bin/bash
# This script sends a GET request to a given URL and displays the body of the response if the status code is 200

response=$(curl -s -o /dev/null -w "%{http_code}" "$1")
if [[ "$response" -eq 200 ]]; then
    curl -s "$1"
fi

