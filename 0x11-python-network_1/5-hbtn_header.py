#!/usr/bin/python3
import requests
import sys

# Obtain the URL using a command-line argument.
url = sys.argv[1]

# Make a GET request to the URL
response = requests.get(url)

# Obtain the response header's X-Request-Id value.
x_request_id = response.headers.get('X-Request-Id')

# Show the X-Request-Id value.
print(x_request_id)
