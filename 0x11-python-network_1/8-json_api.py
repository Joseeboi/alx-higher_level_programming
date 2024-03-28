#!/usr/bin/python3

import requests
import sys

if __name__ == "__main__":
    # Get the letter from command-line arguments or set it to an empty string if no argument is given
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    # Send POST request to the URL with the letter as a parameter
    response = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    
    # Check if the response body is properly JSON formatted and not empty
    try:
        json_response = response.json()
        if json_response:
            # Display id and name if the JSON is not empty
            print("[{}] {}".format(json_response['id'], json_response['name']))
        else:
            # Display No result if the JSON is empty
            print("No result")
    except ValueError:
        # Display Not a valid JSON if the JSON is invalid
        print("Not a valid JSON")
