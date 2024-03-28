#!/usr/bin/python3

import requests
import sys

if __name__ == "__main__":
    # Get repository name and owner name from command-line arguments
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    # Send GET request to GitHub API to retrieve the commits
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extract the 10 most recent commits
        commits = response.json()[:10]

        # Print each commit in the format <sha>: <author name>
        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    else:
        # Print error message if the request was not successful
        print("Failed to retrieve commits. Status code:", response.status_code)
