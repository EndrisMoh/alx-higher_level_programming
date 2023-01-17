#!/usr/bin/python3
"""
A Python script that takes in a URL, sends a request to the URL and displays
the body of the response (decoded in `utf-8`)
You have to manage `urllib.error.HTTPError` exceptions and print:
`Error code`: followed by the HTTP status code
"""
from urllib import request, error
import sys


if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except error.HTTPError as err:
        print('Error code: {}'.format(err.code))
