#!/usr/bin/python3
"""
Module ```0-read_file``` doc
"""


def read_file(filename=""):
    """ Read a file"""
    with open(filename, encoding="utf-8") as fd:
        print(fd.read(), end="")
