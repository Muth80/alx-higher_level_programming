#!/usr/bin/python3
import urllib.request
import urllib.error
import sys

# Obtain the URL using a command-line argument.
url = sys.argv[1]

try:
    # Send an inquiry to the URL.
    with urllib.request.urlopen(url) as response:
        # Read and cipher the body of the response
        response_body = response.read().decode('utf-8')
        # Display the response
        print(response_body)

except urllib.error.HTTPError as e:
    # If an HTTP error occurs, print the error code
    print("Error code: {}".format(e.code))

