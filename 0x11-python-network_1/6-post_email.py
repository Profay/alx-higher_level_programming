#!/usr/bin/python3
""" This module takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""

import requests
import sys


def get_POST_mail():
    """ This function retuens an email using
    POST request.
    """
    url = sys.argv[1]
    email = {'email': sys.argv[2]}
    response = requests.post(url, data=email)
    print(response.text)


if __name__ == "__main__":
    get_POST_mail()
