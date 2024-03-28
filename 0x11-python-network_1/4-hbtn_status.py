#!/usr/bin/python3

import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    
    # Send GET request to the URL
    response = requests.get(url)
    
    # Display the body of the response
    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)
