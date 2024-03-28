#!/usr/bin/python3

import requests
import sys

if __name__ == "__main__":
    # Get the URL from command-line arguments
    url = sys.argv[1]

    # Send request to the URL
    response = requests.get(url)
    
    # Check if the status code is greater than or equal to 400
    if response.status_code >= 400:
        # Print error message with the HTTP status code
        print("Error code:", response.status_code)
    else:
        # Display the body of the response
        print(response.text)
