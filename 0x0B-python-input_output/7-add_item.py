#!/usr/bin/python3
"""
Write a script that adds all arguments
to a Python list, and then save them to a file
"""


from sys import argv
load = __import__('6-load_from_json_file').load_from_json_file
save = __import__('5-save_to_json_file').save_to_json_file

try:
    my_list = load("add_item.json")
except FileNotFoundError:
    my_list = []
for argc in argv[1:]:
    my_list.append(argc)
save(my_list, "add_item.json")
