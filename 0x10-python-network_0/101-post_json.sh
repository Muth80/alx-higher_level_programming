#!/bin/bash
# This script sends a JSON POST request to the provided URL and displays the body of the response

url="$1"
filename="$2"

# Check if the file exists
if [ ! -f "$filename" ]; then
    echo "File '$filename' does not exist"
    exit 1
fi

# Read the file content
content=$(cat "$filename")

# Send the POST request with the file content as the JSON body
response=$(curl -s -X POST -H "Content-Type: application/json" -d "$content" "$url")

echo "$response"

