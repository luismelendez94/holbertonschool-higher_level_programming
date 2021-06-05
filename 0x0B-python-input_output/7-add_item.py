#!/usr/bin/python3
""" Script to add all argument to a python list and save them to a file """

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

import sys

fileName = "add_item.json"

try:
    fileList = load_from_json_file(fileName)
except:
    fileList = []

for arg in sys.argv[1:]:
    fileList.append(arg)

save_to_json_file(fileList, "add_item.json")
