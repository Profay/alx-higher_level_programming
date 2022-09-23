#!/usr/bin/python3
""" My GitGub """
from sys import argv
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    _auth = HTTPBasicAuth(argv[1], argv[2])
    request = requests.get('https://api.github.com/user', auth=_auth)
    print(request.json().get('id'))
