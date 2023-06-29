#!/bin/bash
# This script sends a request to the provided URL and displays only the status code of the response

url="$1"

status_code=$(curl -s -o /dev/null -w "%{http_code}" "$url")

echo "$status_code"

