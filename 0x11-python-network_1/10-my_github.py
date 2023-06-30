#!/usr/bin/python3
import requests
import sys

# Obtain the GitHub user name and personal access token using the command-line argument
username = sys.argv[1]
password = sys.argv[2]

# GitHub API endpoint
url = 'https://api.github.com/user'

# Make a GET request to the GitHub API with Basic Authentication
response = requests.get(url, auth=(username, password))

# Check the response status code
if response.status_code == 200:
    # Get the JSON data from the response
    json_data = response.json()
    # Display the id from the JSON data
    print(json_data['id'])
else:
    # Display None if the authentication fails or other error occurs
    print(None)

