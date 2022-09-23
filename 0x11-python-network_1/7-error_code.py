#!/usr/bin/python3
""" Fetches https://intranet.hbtn.io/status """
import requests
from sys import argv

if __name__ == "__main__":
    request = requests.get(argv[1])

    if request.status_code < 400:
        print(request.text)
    else:
        print('Error code: {}'.format(request.status_code))
