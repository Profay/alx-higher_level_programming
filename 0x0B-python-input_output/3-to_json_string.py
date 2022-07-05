#!/usr/bin/python3
"""
Modules for json string representation
"""
import json



def to_json_string(my_obj):
    """
    This function return the json string representation of the argument recieved
    """
    return json.dumps(my_obj)
