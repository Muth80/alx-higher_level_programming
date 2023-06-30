#!/usr/bin/python3
import requests
import sys

# Get the letter from command-line argument
letter = sys.argv[1] if len(sys.argv) > 1 else ""

# Set the parameters for the POST request
params = {'q': letter}

# Send a POST request to the URL with the letter as a parameter
response = requests.post('http://0.0.0.0:5000/search_user', data=params)

try:
    # Parse the response as JSON
    json_data = response.json()

    if json_data:
        # Display the id and name if the JSON is properly formatted and not empty
        print("[{}] {}".format(json_data.get('id'), json_data.get('name')))
    else:
        # Display "No result" if the JSON is empty
        print("No result")
except ValueError:
    # Display "Not a valid JSON" if the JSON is invalid
    print("Not a valid JSON")

