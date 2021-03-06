#!/usr/bin/python3
"""
Write a Python script that takes in a URL and a email, sends a POST
request to the passed URL with the email as a parameter, and displays
the body of the response
"""


if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    url = sys.argv[1]
    email = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(email).encode('utf8')
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        the_page = response.read().decode('utf-8')
        print(the_page)
