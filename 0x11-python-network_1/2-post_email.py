#!/usr/bin/python3

import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    # Check if the script is called with the URL and email arguments
    if len(sys.argv) != 3:
        print("Usage: python script.py <URL> <email>")
        sys.exit(1)
    
    # Get the URL and email from command-line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Encode the email parameter
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    # Send POST request to the URL with the email as a parameter
    with urllib.request.urlopen(url, data=data) as response:
        # Read and decode the body of the response
        body = response.read().decode('utf-8')
        
        # Display the body of the response
        print(body)
