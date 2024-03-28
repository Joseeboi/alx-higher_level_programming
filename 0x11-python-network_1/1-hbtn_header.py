#!/usr/bin/python3

import urllib.request
import sys

if __name__ == "__main__":
    # Check if the script is called with the URL argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)
    
    # Get the URL from command-line arguments
    url = sys.argv[1]

    # Send request to the URL and get the response
    with urllib.request.urlopen(url) as response:
        # Get the value of the X-Request-Id variable from the header
        x_request_id = response.getheader('X-Request-Id')
        
        if x_request_id:
            print(x_request_id)
        else:
            print("X-Request-Id header not found in the response.")
