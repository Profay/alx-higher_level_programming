#!/usr/bin/python3
"""
Modules for json string representation
"""
import json


def from_json_string(my_str):
    """
    This function return the python data structure json
    string representation of the argument recieved
    """
    return json.loads(my_str)
