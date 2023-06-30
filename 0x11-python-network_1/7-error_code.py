#!/usr/bin/python3
import requests
import sys

# Obtain the URL from a command-line argument.
url = sys.argv[1]

# Make a GET request to the URL.
response = requests.get(url)

# Check the status code of the response
if response.status_code >= 400:
    # Print error message if status code is greater than or equal to 400
    print("Error code: {}".format(response.status_code))
else:
    # Print the body of the response
    print(response.text)

