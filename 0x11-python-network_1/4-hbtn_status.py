#!/usr/bin/python3
import requests

# Retrieve URL
url = 'https://alx-intranet.hbtn.io/status'

# Send a GET request to the URL.
response = requests.get(url)

# Show the response's body in the preferred format.
print("Body response:")
print("\t- type: {}".format(type(response.text)))  # Print the type of the content
print("\t- content: {}".format(response.text))  # Print the content
