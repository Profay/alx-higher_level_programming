#!/usr/bin/python3
""" This module takes in a URL and print error
status code.
"""

import requests
import sys


def error_status():
    """ This function prints an error status code.
    """
    url = sys.argv[1]
    response = requests.get(url)
    if requests.status_codes >= 400:
        print('Error code: {}'.format(request.status_code))


if __name__ == "__main__":
    error_status()
