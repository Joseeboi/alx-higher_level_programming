#!/usr/bin/python3

import requests
import sys

if __name__ == "__main__":
    # Get the URL from command-line arguments
    url = sys.argv[1]

    # Send request to the URL
    response = requests.get(url)
    
    # Check if X-Request-Id is present in the response header
    if 'X-Request-Id' in response.headers:
        # Get and print the value of X-Request-Id
        x_request_id = response.headers['X-Request-Id']
        print(x_request_id)
    else:
        print("X-Request-Id header not found in the response.")
