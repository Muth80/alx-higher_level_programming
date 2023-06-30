#!/usr/bin/python3
import urllib.request
import sys

# Obtain the URL using a command-line argument.
url = sys.argv[1]

# Make a request to the URL.
with urllib.request.urlopen(url) as response:
    # Obtain the response header's X-Request-Id value.
    x_request_id = response.getheader('X-Request-Id')

# Show the X-Request-Id value.
print(x_request_id)
