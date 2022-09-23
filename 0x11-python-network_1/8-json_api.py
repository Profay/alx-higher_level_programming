#!/usr/bin/python3
""" Fetches https://intranet.hbtn.io/status """
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) == 1:
        value = {'q': ''}
    else:
        value = {'q': argv[1]}

    request = requests.post("http://0.0.0.0:5000/search_user", data=value)
    try:
        my_dict = request.json()
        if len(my_dict) == 0:
            print("No result")
        else:
            print("[{}] {}".format(my_dict["id"], my_dict["name"]))
    except ValueError:
        print("Not a valid JSON")
