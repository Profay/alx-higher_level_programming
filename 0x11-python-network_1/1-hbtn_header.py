#!/usr/bin/python3
""" This module takes in a URL, sends a request
to the URL and displays the value of the X-Request-Id
variable found in the header of the response.
"""

import urllib.request
import sys


def get_request_id():
    """ This function returns the X-Request-Id
    variable found in the header of the response.
    """
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as req:
        print(req.headers.get("X-Request-Id"))


if __name__ == "__main__":
    get_request_id()
