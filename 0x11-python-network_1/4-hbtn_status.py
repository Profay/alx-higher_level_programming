#!/usr/bin/python3
""" This module uses request to fecth url body
responses from https://alx-intranet.hbtn.io/status
"""

import requests


def get_request():
    """ This function uses request to fecth url body
    responses from https://alx-intranet.hbtn.io/status
    """
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    r = response.text
    print("Body response:")
    print("\t- type: {}".format(type(r)))
    print("\t- content: {}".format(r))


if __name__ == "__main__":
    get_request()
