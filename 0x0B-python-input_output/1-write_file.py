#!/usr/bin/python3
"""
Module ```1-write_file``` doc
"""


def write_file(filename="", text=""):
    """ Write to a file"""
    with open(filename, "w", encoding="utf-8") as fd:
        f_write = fd.write(text)
    return f_write
