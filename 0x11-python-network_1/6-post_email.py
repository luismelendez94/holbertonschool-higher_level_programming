#!/usr/bin/python3
"""
Write a Python script that takes in a URL and an email,
sends a POST request to the URL with the email and
displays the body of the response.
"""

import requests
import sys

if __name__ == "__main__":

    url = sys.argv[1]
    email = {"email": sys.argv[2]}

    print(requests.post(url, data=email).text)
