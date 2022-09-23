#!/usr/bin/python3
""" This module that takes in a URL, sends a request
to the URL and displays the body of the response
(decoded in utf-8).
:::
    manage urllib.error.HTTPError exceptions and print:
    Error code: followed by the HTTP status code

"""

from urllib import parse, request
from sys import argv


def error_response():
    """ This function takes in a URL, sends a request
    to the URL and displays the body of the response
    (decoded in utf-8).
    """
    url = argv[1]
    req = request.Request(url)
    try:
        with request.urlopen(req) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        error_code = e.code().decode('utf-8')
        print("Error code: {}".format(error_code))
