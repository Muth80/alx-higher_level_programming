#!/usr/bin/python3
import urllib.request

# To get back URL
url = 'https://alx-intranet.hbtn.io/status'

# Open the URL and obtain the outcome.
with urllib.request.urlopen(url) as response:
    content = response.read()

# Print the body of the response in the preferred manner.
print("Body response:")
print("\t- type: {}".format(type(content)))  # Print the content's type.
print("\t- content: {}".format(content))  # Print the original code.
print("\t- utf8 content: {}".format(content.decode('utf-8')))  # Print the content decoded as UTF-8
