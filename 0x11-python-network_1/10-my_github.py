#!/usr/bin/python3

import requests
import sys

if __name__ == "__main__":
    # Get GitHub username and personal access token from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]

    # Create Basic Authentication string using the personal access token
    auth = (username, password)

    # Send GET request to GitHub API to retrieve user information
    response = requests.get('https://api.github.com/user', auth=auth)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extract user id from the JSON response
        user_id = response.json()['id']
        print("Your GitHub user id is:", user_id)
    else:
        # Print error message if the request was not successful
        print("Failed to retrieve user information. Status code:", response.status_code)
