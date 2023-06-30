#!/usr/bin/python3
import requests
import sys

# Get the repository name and owner name from command-line arguments
repo_name = sys.argv[1]
owner_name = sys.argv[2]

# Set the GitHub API endpoint for retrieving commits
url = f'https://api.github.com/repos/{owner_name}/{repo_name}/commits'

# Send a GET request to the GitHub API
response = requests.get(url)

# Check the response status code
if response.status_code == 200:
    # Get the JSON data from the response
    json_data = response.json()
    # Iterate over the 10 most recent commits
    for commit in json_data[:10]:
        # Extract the commit sha and author name
        sha = commit['sha']
        author = commit['commit']['author']['name']
        # Print the commit information
        print(f'{sha}: {author}')
else:
    # Display an error message if the request fails
    print('Error: Failed to retrieve commits')

