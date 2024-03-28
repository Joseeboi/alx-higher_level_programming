#!/usr/bin/python3

import requests
import sys

if __name__ == "__main__":
    # Get the URL and email address from command-line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Create a dictionary with the email parameter
    data = {'email': email}

    # Send a POST request to the URL with the email as a parameter
    response = requests.post(url, data=data)
    
    # Display the body of the response
    print(response.text)
