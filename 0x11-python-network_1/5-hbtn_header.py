#!/usr/bin/python3
""" This module uses request to fecth url header
id from https://alx-intranet.hbtn.io/status
"""

import requests
import sys


def get_request():
    """ This function uses request to fecth url header
    id from url
    """
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get("X-Request-Id"))


if __name__ == "__main__":
    get_request()
