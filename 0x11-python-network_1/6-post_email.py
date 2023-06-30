#!/usr/bin/python3
import requests
import sys

# Obtain the URL and email address from command-line parameters.
url = sys.argv[1]
email = sys.argv[2]

# Generate a dictionary with the email argument.
data = {'email': email}

# Send a POST request with the email parameter to the URL.
response = requests.post(url, data=data)

# Display the body of the response
print(response.text)

