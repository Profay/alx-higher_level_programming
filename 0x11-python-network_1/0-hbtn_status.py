#!/usr/bin/python3
""" This module fetches https://alx-intranet.hbtn.io/status
"""

import urllib.request


def get_alx_status():
    """ This function fetches https://alx-intranet.hbtn.io/status
    """
    url = "https://alx-intranet.hbtn.io/status"
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as resp:
        html = resp.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode('utf-8')))


if __name__ == "__main__":
    get_alx_status()
