#!/usr/bin/python3
import urllib.parse
import urllib.request
import sys

# Obtain the URL and email using command-line parameters.
url = sys.argv[1]
email = sys.argv[2]

# cipher the email parameter
data = urllib.parse.urlencode({'email': email}).encode('utf-8')

# Make a POST request with the email parameter to the URL.
with urllib.request.urlopen(url, data) as response:
    # Read and cipher the body of the response
    response_body = response.read().decode('utf-8')

# Display the response
print(response_body)

