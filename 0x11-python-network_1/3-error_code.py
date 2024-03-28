#!/usr/bin/python3

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    # Check if the script is called with the URL argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)
    
    # Get the URL from command-line arguments
    url = sys.argv[1]

    try:
        # Send request to the URL and get the response
        with urllib.request.urlopen(url) as response:
            # Read and decode the body of the response
            body = response.read().decode('utf-8')
            
            # Display the body of the response
            print(body)
    except urllib.error.HTTPError as e:
        # Handle HTTPError exception
        print("Error code:", e.code)
