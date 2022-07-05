#!/usr/bin/python3
"""
Define the save_to_json_file function
"""
import json


def load_from_json_file(filename):
    """ The function writes an Object to a text file,
    using a JSON representation """
    with open(filename, "r", encoding='utf-8') as file:
        return (json.loads(file.read))
